import cv2 as cv
import numpy as np
import sys
import os
import subprocess
from glob import glob

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

imdir = os.path.dirname(sys.argv[1])
size = imagem_src.shape[0]
cv.imwrite('{}/gfr_{:03d}.png'.format(imdir, 0), imagem_src)
cv.imwrite('{}/gfr_{:03d}.png'.format(imdir, iteracoes * 2), imagem_dst)

for i in xrange(1, iteracoes):
    sizediv = 2 ** (i + 1)
    output = cv.resize(imagem_src, (size / sizediv, size / sizediv))
    output = np.repeat(output, sizediv, axis=0)
    output = np.repeat(output, sizediv, axis=1)
    cv.imwrite('{}/gfr_{:03d}.png'.format(imdir, i), output)
    output = cv.resize(imagem_dst, (size / sizediv, size / sizediv))
    output = np.repeat(output, sizediv, axis=0)
    output = np.repeat(output, sizediv, axis=1)
    cv.imwrite('{}/gfr_{:03d}.png'.format(
        imdir, (iteracoes * 2) - 1 - i), output)

print('Criando GIF...')
if subprocess.check_call(['convert', '-delay', '20', '-loop', '0',
                          '{}/gfr_*.png'.format(imdir),
                          '{}/output.gif'.format(imdir)]):
    print('PRONTO')
print('Limpando...')
for file in glob('{}/gfr_*.png'.format(imdir)):
    os.remove(file)