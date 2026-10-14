import depthai as dai
import cv2

with dai.Pipeline() as pipeline:

    cam = pipeline.create(dai.node.Camera).build()

    video_queue = cam.requestOutput(
        (1280, 720),
        fps=15
    ).createOutputQueue(maxSize=1, blocking=False)

    pipeline.start()

    print("Camera running.")
    print("Press Q to quit.")

    cv2.namedWindow("OAK-D RGB", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("OAK-D RGB", 800, 450)

    while pipeline.isRunning():

        frame_packet = video_queue.tryGet()

        if frame_packet is not None:
            frame = frame_packet.getCvFrame()
            cv2.imshow("OAK-D RGB", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
