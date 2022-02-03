img = imread('figs/pollen.tif');

img2 = histeq(img); % histogram equalization

figure
subplot(221); imshow(img) % subplot can be used to plot several images in one figure
subplot(222); imshow(img2)
subplot(223); imhist(img) % displays histogram of the image
subplot(224); imhist(img2)
