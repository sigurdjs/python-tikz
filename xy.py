import numpy

def generate_xy_plot(x_axis, y_axises, names, filename = None, second_y_axises = None, colors = None,
                     x_label = None, y_label = None, second_y_label = None, x_tick = None, x_tick_labels = None,
                     x_tick_labels_rotation = None, legend_placement = None, title = None, plot_shape = None,
                     line_thickness = None):

    (y_min, y_max) = get_y_maxmin(y_axises)
    tex_string = ""
    if colors != None and colors[0][0] == '#':
        for i, color in enumerate(colors):
            tex_string += "\\definecolor{color" + str(i) + "}{HTML}{" + color[1:] + "}\n"

    tex_string += "\\begin{tikzpicture}[trim axis left, trim axis right]\n"

    if line_thickness != None:
        tex_string += "\\pgfplotsset{every axis plot post/.append style={" + line_thickness + "}}\n"

    tex_string += "\\begin{axis}[\n"
    if plot_shape != None:
        if plot_shape.lower() == 'rectangular':
            tex_string += "width = \\textwidth,\n"
            tex_string += "height = 0.625*\\textwidth,\n"

        elif plot_shape.lower() == 'square':
            tex_string += "width = 0.625\\textwidth,\n"
            tex_string += "height = 0.625\\textwidth,\n"
    else:
        tex_string += "width = \\textwidth,\n"
        tex_string += "height = 0.625*\\textwidth,\n"

            
    if title != None:
        tex_string += "title = {" + title + "},\n"
    
    
    
    if second_y_axises != None:
        tex_string += "axis y line=left,\n"
    if x_label != None:
        tex_string += "xlabel = {" + x_label + "},\n"
    if y_label != None:
        tex_string += "ylabel = {" + y_label + "},\n"
    if x_tick != None and x_tick_labels != None:
        tex_string += "xtick = {" + ', '.join(str(item) for item in x_tick) + "},\n"
        tex_string += "xticklabels = {" + ', '.join(str(item) for item in x_tick_labels) + "},\n"
    
    if x_tick_labels_rotation != None:
        tex_string += "x tick label style = {rotate = " + str(x_tick_labels_rotation) + "},\n"

    tex_string += "ticklabel style = {font = \\footnotesize},\n"

    if legend_placement != None:
        if legend_placement.lower() == 'north west':
            tex_string += "legend style = {font = \\footnotesize, at={(0.02,0.98)},anchor=north west},\n"
        elif legend_placement.lower() == 'south west':
            tex_string += "legend style = {font = \\footnotesize, at={(0.02,0.02)},anchor=south west},\n"
        elif legend_placement.lower() == 'south east':
            tex_string += "legend style = {font = \\footnotesize, at={(0.98,0.02)},anchor=south east},\n"
        elif legend_placement.lower() == 'north east':
            tex_string += "legend style = {font = \\footnotesize, at={(0.98,0.98)},anchor=north east},\n"
    else:
        tex_string += "legend style = {font = \\footnotesize},\n"
    
    tex_string += "label style = {font = \\footnotesize},\n"
    tex_string += "xmin = " + str(min(x_axis)) + ",\n"
    tex_string += "xmax = " + str(max(x_axis)) + ",\n"
    tex_string += "ymin = " + str(y_min) + ",\n"
    tex_string += "ymax = " + str(y_max) + "\n]\n"

    if colors == None:
        colors = ['red', 'blue','yellow','green']
    else:
        colors = ['color' + str(i) for i, _ in enumerate(colors)]
    
    for i, axis in enumerate(y_axises):
        tex_string += "\\addplot [semithick, " + colors[i] + "]\n"
        tex_string += "table{\n"

        for j, y in enumerate(axis):
            tex_string += str(x_axis[j]) + ' ' + str(y) + '\n'

        if second_y_axises != None:
            tex_string += '}; \\label{' + str(i) + '}\n'
        else:
            tex_string += '};\n'
            tex_string += "\\addlegendentry{" + names[i] + "}\n\n"

    tex_string += "\\end{axis}\n"



    if second_y_axises != None:

        (y_min, y_max) = get_y_maxmin(second_y_axises)

        tex_string += "\\begin{axis}[\n"
        tex_string += "width = \\textwidth,\n"
        tex_string += "height = 0.625*\\textwidth,\n"
        tex_string += "axis y line=right,\n"
        if second_y_label != None:
            tex_string += "ylabel = {" + second_y_label + "},\n"
        tex_string += "ticklabel style = {font = \\footnotesize},\n"
        tex_string += "legend style = {font = \\footnotesize},\n"
        tex_string += "label style = {font = \\footnotesize},\n"
        tex_string += "xmin = " + str(min(x_axis)) + ",\n"
        tex_string += "xmax = " + str(max(x_axis)) + ",\n"
        tex_string += "ymin = " + str(y_min) + ",\n"
        tex_string += "ymax = " + str(y_max) + "\n]\n"

        for i in range(0,len(y_axises)):
            tex_string += "\\addlegendimage{/pgfplots/refstyle=" + str(i) + "}\\addlegendentry{" + names[i] + "}\n"


        for i, axis in enumerate(second_y_axises):
            idx = i + len(y_axises)
            tex_string += "\\addplot [semithick, " + colors[idx] + "]\n"
            tex_string += "table{\n"

            for j, y in enumerate(axis):
                tex_string += str(x_axis[j]) + ' ' + str(y) + '\n'

            tex_string += '};\n'
            tex_string += "\\addlegendentry{" + names[idx] + "}\n\n"

        tex_string += "\\end{axis}\n"

    tex_string += "\\end{tikzpicture}\n"


    if filename == None:
        filename = 'figure'

    with open(filename + '.tex', 'w+') as f:

        f.write(tex_string)

def get_y_maxmin(y_axises):

    y_min = min(numpy.concatenate(y_axises))
    y_max = max(numpy.concatenate(y_axises))

    diff = abs(y_max - y_min)

    y_min = y_min - 0.05*diff
    y_max = y_max + 0.05*diff

    return(y_min, y_max)