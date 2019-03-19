# The data is a list of tuples where the first element is the group name
def generate_bar_plot(data, filename = None, x_label = None, y_label = None,
                        legend_names = None, rotate_x_ticks = False):

    symbolic_coords = [item[0] for item in data]

    data_size = len(data[0][1:])

    tex_string  = "\\begin{tikzpicture}[trim axis left, trim axis right]\n"
    tex_string += "\\begin{axis}[\n"
    tex_string += "symbolic x coords={" + ', '.join(symbolic_coords) + "},\n"
    tex_string += "width = \\textwidth,\n"
    tex_string += "height = 0.625*\\textwidth,\n"
    if x_label != None:
        tex_string += "xlabel = {" + x_label + "},\n"
    if y_label != None:
        tex_string += "ylabel = {" + y_label + "},\n"
    tex_string += "ticklabel style = {font = \\footnotesize},\n"
    if rotate_x_ticks == True:
        tex_string += "x tick label style={rotate=90},\n"
    tex_string += "legend style = {font = \\footnotesize},\n"
    tex_string += "label style = {font = \\footnotesize},\n"
    tex_string += "ymin = 0,\n"
    tex_string += "ybar=3*\\pgflinewidth,\n"
    tex_string += "bar width=0.26cm,\n"
    tex_string += "xtick = data]\n"

    colors = ['red', 'blue', 'green', 'yellow']

    for i in range(0, data_size):
        tex_string += "\\addplot[ybar, fill = " + colors[i] + "] coordinates { \n"
        for item in data:
            tex_string += "(" + item[0] + "," + str(item[i + 1]) + ")\n"

        tex_string += "};\n"

    if legend_names != None:
        tex_string += "\\legend{" + ', '.join(legend_names) + "}\n"

    tex_string += "\\end{axis}\n"
    tex_string += "\\end{tikzpicture}"

    if filename == None:
        filename = 'figure'

    with open(filename + '.tex', 'w+') as f:
        f.write(tex_string)

if __name__ == "__main__":
    data = [('Group', 1, 3, 4, 5)]
    generate_bar_plot(data)