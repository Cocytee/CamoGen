using FileIO
using PyPlot
using Images
using FFTW

mutable struct CamoDB
	EigenVector :: Array{Float64,1}
	TerrainList :: Array{AbstractString,1}
	TerrainDB :: Dict{AbstractString,Terrain}
end

mutable struct Terrain
	PopList :: Array{AbstractString,1}
	PopSize :: Int
	StatAvg :: Array{Float64,1}
	StatPopulation :: Array{Float64,2}
	EigenAvg :: Array{Float64,1}
	EigenPopulation :: Array{Float64,2}
end


function buildStat(folder::AbstractString,resolution::Int)
	#list the files
	pl = filter(x -> x[end-1:end]=="md", folder .* readdir(folder))
	ps = length(imglist)
	#transform each image in statistic features
	data = zeros(ps,(resolution^2)*3*2)
	for (n,img) in enumerate(imglist)
		data[n,:] = statify(img)
	end	

	#WIP

end

#extract statistical inof from a pics
function statify(imgName::AbstractString)

	#WIP
	
end

#Convenient frequency tranform for human eyes
freqview(A) = 100 .*log.(abs.(1 .+ real.(A)))

#Statistical info display - NEED WORK
function ImageInfo(imgName::AbstractString,resolution::Int)
	img = channelview(load(imgName))
	(h,l)= size(img)[2:3]
	ms = minimum((h,l))
	imgR = img[:,1:ms,1:ms]
	imgF = fftshift(fft(imgR))
	imgFR= imresize(imgF, 3, resolution, resolution)

	figure(1)
	for i in 1:3
		subplot(3,4,1+(i-1)*4)
		imshow(img[i,:,:])
		subplot(3,4,2+(i-1)*4)
		imshow(imgR[i,:,:])
		subplot(3,4,3+(i-1)*4)
		imshow(freqview(imgF[i,:,:]))
		subplot(3,4,4+(i-1)*4)
		imshow(freqview(imgFR[i,:,:]))
	end

	figure(2)
	StatTotal = vec([imgFR[1,:,:] imgFR[2,:,:] imgFR[3,:,:]])
	plot(1:length(StatTotal),real.(StatTotal),"g,")
	plot(1:length(StatTotal),imag.(StatTotal),"c,")
end