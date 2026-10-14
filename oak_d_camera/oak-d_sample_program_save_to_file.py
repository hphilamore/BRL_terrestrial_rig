import depthai as dai
import cv2
from datetime import datetime

# Video settings
width = 1280
height = 720
fps = 15

# Create a unique filename using the current date and time
filename = datetime.now().strftime("oakd_%Y%m%d_%H%M%S.mp4")

with dai.Pipeline() as pipeline:

    cam = pipeline.create(dai.node.Camera).build()

    video_queue = cam.requestOutput(
        (width, height),
        fps=fps
    ).createOutputQueue(maxSize=1, blocking=False)

    pipeline.start()

    # Initialise the MP4 video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(
        filename,
        fourcc,
        fps,
        (width, height)
    )

    if not video_writer.isOpened():
        raise RuntimeError("Could not open video file for writing.")

    print(f"Recording to {filename}")
    print("Press Q to stop recording.")

    cv2.namedWindow("OAK-D RGB", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("OAK-D RGB", 800, 450)

    try:
        while pipeline.isRunning():

            frame_packet = video_queue.tryGet()

            if frame_packet is not None:
                frame = frame_packet.getCvFrame()

                # Write frame to MP4 file
                video_writer.write(frame)

                # Display live video
                cv2.imshow("OAK-D RGB", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Finalise the video file
        video_writer.release()
        cv2.destroyAllWindows()

        print(f"Video saved to {filename}")