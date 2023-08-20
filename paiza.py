import copy

def padding_zero(num, val_dict):
    val_dict_copy = copy.deepcopy(val_dict)
    summit_list = []
    dummy = [9 for _ in range(num + 2)]
    
    for i in range(num + 2):
        if i == 0:
            summit_list.append(dummy)
        elif i == num + 1:
            summit_list.append(dummy)
        else:
            val_dict_copy[i].insert(0, 9)
            val_dict_copy[i].append(9)
            summit_list.append(val_dict_copy[i])
            
    return summit_list


def converting_from_color_to_number(color_dict, color):
    data = copy.deepcopy(color_dict)
    
    for y in data:
        for x in range(len(data[y])):
            if color == data[y][x]:
                data[y][x] = 1
            else:
                data[y][x] = 9
    return data


class Color:
    def __init__(self, data_list, h, w, color):
        self.data_list = data_list
        self.h = h + 1
        self.w = w + 1
        self.color = color
        self.x = 0
        self.y = 0
        self.target = 1
        self.result_dict = {'R': 0, 'G': 0, 'B': 0}
    
    def color_search_start_point(self):

        while True:
            if self.x < self.w: 
                self.x += 1
            elif self.y < self.h:
                self.y += 1
                self.x = 1
            elif self.x == self.w and self.y == self.h: 
                break

            if self.target == self.data_list[self.y][self.x]:
                break
        
    def target_data_confirmation_recursively(self, data):
        
        return [ j for i in data for j in i ]

        
    def color_end_point(self):
        
        self.data_list[self.y][self.x] = 3
        
        start_y = self.y
        start_x = self.x
        
        while True:
                
            if self.data_list[self.y-1][self.x] < 2:
                self.data_list[self.y-1][self.x] = 2
                self.y -= 1
                continue
            elif self.data_list[self.y][self.x+1] < 2:
                self.data_list[self.y][self.x+1] = 2
                self.x += 1
                continue
            elif self.data_list[self.y+1][self.x] < 2:
                self.data_list[self.y+1][self.x] = 2
                self.y += 1
                continue
            elif self.data_list[self.y][self.x-1] < 2:
                self.data_list[self.y][self.x-1] = 2
                self.x -= 1
                continue
            else:
                self.data_list[start_y][start_x] = 2
                break
            
        self.result_dict[self.color] += 1
        
                    
    def target_color(self, data_count):
        count = 0
        while True:
            if self.target_data_confirmation_recursively(self.data_list)[count] == self.target:
                self.color_search_start_point()
                self.color_end_point()
                count = 0
                self.y = 0
                self.x = 0
                
            count += 1
            
            if count == data_count:
                break
            
        return self.result_dict[self.color]


if __name__ == "__main__":
    h, w = map(int, input().split())
    color_dict = {}
    for i in range(1, h+1):
        color_dict[i] = list(str(input()))

    color = ['R', 'G', 'B']
    
    result = {'R': 0, 'G': 0, 'B': 0}
    
    all_count = (h+2) * (w+2)
    
    for c in color:
        con_from_color_to_num_dict = converting_from_color_to_number(color_dict, c)
        
        color_list = padding_zero(h, con_from_color_to_num_dict)
        
        color = Color(color_list, h, w, c)
        result[c] = color.target_color(all_count)
        
    print(result["R"], result["G"], result["B"])
    