% Machine Vision 2022, Exercises 1

%% Task 1

%   MATLAB'S CELL MODE (for scripts):
%   Double percentage signs (%%) mark the beginning of a cell.
%   To move quickly between cells: CTRL + ARROW KEY UP/DOWN
%   Run cell: CTRL + ENTER


clear all  % clears workspace
close all  % closes all open figures

f = imread('figs/mammogram.tif');  % read image file to variable

figure
imshow(f) % show image in figure


%%

j = imadjust(f,'',[1 0]); % negative image is get when parameter high_out < low_out
figure
imshow(j)


%% Task 2

clear all
close all

img = imread('figs/pollen.tif');

img2 = histeq(img); % histogram equalization

figure
subplot(221); imshow(img) % subplot can be used to plot several images in one figure
subplot(222); imshow(img2)
subplot(223); imhist(img) % displays histogram of the image
subplot(224); imhist(img2)


%% Task 3

clear all
close all

img = imread('figs/pollen.tif');

img2 = histeq(img);

im = myfunction(img,1,200,300,500); % function call for function called myfunction, which is in m-file myfunction.m

im2 = myfunction(img2,1,200,300,500);

figure
subplot(221); imshow(im)
subplot(222); imshow(im2)
subplot(223); imshow(img)
subplot(224); imshow(img2)

