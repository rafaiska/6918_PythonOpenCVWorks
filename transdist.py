import numpy as np
import cv2 as cv


def min_manhattan_dist(origem, bordas):
    min = 255
    for borda_pix in bordas:
        distancia = abs(borda_pix[0] - origem[0]) + abs(borda_pix[1] - origem[1])
        if distancia < min:
            min = distancia
    return min


def find_bordas(img):
    ret_val = []
    for i in xrange(img.shape[0]):
        for j in xrange(img.shape[1]):
            borda_pix = None
            # se for fundo
            if img[i][j] == 0:
                for neighbor in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if (img[i][j] == 0 and
                            0 < neighbor[0] < img.shape[0] and
                            0 < neighbor[1] < img.shape[1] and
                            img[neighbor[0]][neighbor[1]] != 0):
                        borda_pix = (i, j)
                        break
            if borda_pix is not None:
                ret_val.append(borda_pix)
    return ret_val


def transdist(img):
    ret_val = np.ndarray(img.shape, dtype=np.uint8)
    bordas = find_bordas(img)

    for i in xrange(img.shape[0]):
        for j in xrange(img.shape[1]):
            if img[i][j] != 0:
                ret_val[i][j] = min_manhattan_dist((i, j), bordas)
                print('ret_val[{}][{}] = {}'.format(i, j, ret_val[i, j]))
    # print(ret_val)
    return ret_val


def main():
    original = cv.imread('img/dova_small.png', 0)
    # original = cv.imread('/home/rafael/Imagens/CAPA-4.jpg', 0)
    cv.imshow('original tons cinza', original)
    _, limiarizada = cv.threshold(original, 127, 255, cv.THRESH_OTSU)
    cv.imshow('limiar otsu', limiarizada)
    transf_dist = transdist(limiarizada)
    cv.imshow('transdist', transf_dist)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
