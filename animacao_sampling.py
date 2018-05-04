import cv2 as cv
import numpy as np
import sys

if len(sys.argv) < 3:
    print('Parametros insuficientes')
    sys.exit(0)

imagem_src = cv.imread(sys.argv[1])
imagem_dst = cv.imread(sys.argv[2])

for imagem in [imagem_src, imagem_dst]:
    if imagem.shape[0] != imagem.shape[1]:
        print('Imagens devem ser quadradas')
        sys.exit(0)

size = imagem_src.shape[0]
iteracoes = 0
while size > 1:
    size /= 2
    iteracoes += 1

for i in xrange(iteracoes):
    size = imagem_src.shape[0]
    sizediv = 2 ** (i + 1)
    output = cv.resize(imagem_src, (size/sizediv, size/sizediv))
    output = np.repeat(output, sizediv, axis=0)
    output = np.repeat(output, sizediv, axis=1)
    cv.imwrite('/home/rafael/Imagens/{}.png'.format(i), output)
