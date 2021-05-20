using DelimitedFiles
using Plots

range = -50:0.01:50
xs = rand(range, 250)
ys = rand(range, 250)

filter = abs.(xs .- ys) .> 10
xs = xs[filter]
ys = ys[filter]

scatter(xs, ys, label=nothing, size=(500, 500))
plot!(range, range, label=nothing)

savefig("dataset.png")

dataset = hcat(xs, ys, xs .- ys .< 0)
writedlm("dataset.csv", dataset, ',')
