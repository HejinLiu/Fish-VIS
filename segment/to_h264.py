import numpy as np
import cv2 as cv
# import ffmpeg
import imageio as iio
from PIL import Image


def video_trans_size(input_mp4, output_h264):
    cap = cv.VideoCapture(input_mp4)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    print(width, height)

    # 定义编解码器并创建VideoWriter对象
    out = iio.get_writer(output_h264, format='ffmpeg', mode='I', fps=25,
                         codec='libx264', pixelformat='yuv420p', macro_block_size=None)
    while (True):
        ret, frame = cap.read()
        if ret is True:

            image = frame[:, :, (2, 1, 0)]
            # 写翻转的框架
            # out.write(frame)
            out.append_data(image)
            # cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        else:
            break
    # 完成工作后释放所有内容
    cap.release()
    out.close()
    cv.destroyAllWindows()


if __name__ == '__main__':
    video_trans_size('video/t_inovation_8_1.mp4', 'video/t_inovation_8_1h264.mp4')
