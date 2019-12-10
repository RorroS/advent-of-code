f = open("../input/8", "r")
data = [num for num in f.read().rstrip()]
f.close()

WIDTH = 25
HEIGHT = 6
BLACK = 0
WHITE = 1
TRANSPARENT = 2
LEN_OF_LAYER = HEIGHT*WIDTH
AMNT_OF_LAYERS = len(data)//LEN_OF_LAYER

def get_layers(data):
    layers = []

    for i in range(AMNT_OF_LAYERS):
        layers.append([])
        for j in range(LEN_OF_LAYER):
            layers[i].append(int(data[j+LEN_OF_LAYER*i]))

    return layers


def get_fewest_0_layer(layers):
    fewest_0 = LEN_OF_LAYER*2
    fewest_0_layer = None
    for layer in layers:
        current_0 = layer.count(0)
        if current_0 < fewest_0:
            fewest_0 = current_0
            fewest_0_layer = layer
    return fewest_0_layer


def get_pixel_image(layers):
    current_index = 0
    result_layer = []
    while current_index < LEN_OF_LAYER:
        for layer in layers:
            pixel = layer[current_index]
            if pixel != TRANSPARENT:
                result_layer.append(pixel)
                current_index += 1
                break
    return result_layer


def solve_part_two():
    layers = get_layers(data)
    image = get_pixel_image(layers)
    print("p2:")
    for x in range(HEIGHT):
        for y in range(WIDTH):
            print("#" if image[y+WIDTH*x] == 1 else " ", end="")
        print("")


def solve_part_one():
    layers = get_layers(data)
    layer = get_fewest_0_layer(layers)
    amnt_1 = layer.count(1)
    amnt_2 = layer.count(2)
    return amnt_1 * amnt_2


if __name__ == '__main__':
    print("p1:", solve_part_one())
    solve_part_two()
