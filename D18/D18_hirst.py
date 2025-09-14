import colorgram


def color_extract(image,num):
    colors_list=colorgram.extract(image,num)

    ind_colors=[]

    for a in colors_list:
        r_=a.rgb.r
        g_=a.rgb.g
        b_=a.rgb.b
        ind_colors.append((r_,g_,b_))

    return ind_colors

#print(color_extract('image.jpg',10))