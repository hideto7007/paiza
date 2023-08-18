import copy

def padding_zero(num, val_dict):
    val_dict_copy = copy.deepcopy(val_dict)
    summit_list = []
    dummy = ["*" for _ in range(num + 2)]
    
    for i in range(num + 2):
        if i == 0:
            summit_list.append(dummy)
        elif i == num + 1:
            summit_list.append(dummy)
        else:
            val_dict_copy[i].insert(0, "*")
            val_dict_copy[i].append("*")
            summit_list.append(val_dict_copy[i])
            
    return summit_list


class Color:
    def __init__(self, data_list, h, w, color):
        self.data_list = data_list
        self.h = h + 1
        self.w = w + 1
        self.color = color
        self.x = 0
        self.y = 0
    
    def color_search_start_point(self):

        while True:
            if self.x < self.w: 
                self.x += 1
            elif self.y < self.h:
                self.y += 1
                self.x = 1
            elif self.x == self.w and self.y == self.h: 
                break

            if self.color in self.data_list[self.y][self.x]:
                break
    
    def color_end_point(self):
        
        # 通過したことを意味する変数
        passing = self.color + "p"
        
        idx = 0
        
        # TBD:このソースだと一度通過したところでも、カラーの文字が含まれていれば
        # そこに戻ってしまう。
        
        while True:
            if self.color == self.data_list[self.y][self.x] and idx != 0:
                break
                
            if self.color in self.data_list[self.y-1][self.x]:
                self.data_list[self.y-1][self.x] = passing
                self.y -= 1
                idx += 1
                continue
            elif self.color in self.data_list[self.y][self.x+1]:
                self.data_list[self.y][self.x+1] = passing
                self.x += 1
                idx += 1
                continue
            elif self.color in self.data_list[self.y+1][self.x]:
                self.data_list[self.y+1][self.x] = passing
                self.y += 1
                idx += 1
                continue
            elif self.color in self.data_list[self.y][self.x-1]:
                self.data_list[self.y][self.x-1] = passing
                self.x -= 1
                idx += 1
                continue
            else:
                break

                    
    def target_color(self):
        self.color_search_start_point()
        self.color_end_point()
        
        print(self.y, self.x)

        for i in self.data_list:
            print(i)


if __name__ == "__main__":
    # h, w = map(int, input().split())
    # color_dict = {}
    # for i in range(1, h+1):
    #     color_dict[i] = list(str(input()))
    
    h, w = 5, 5
    
    color_dict = {
        1: ['R', 'R', 'R', 'G', 'G'],
        2: ['R', 'R', 'R', 'G', 'G'],
        3: ['B', 'B', 'B', 'B', 'B'],
        4: ['R', 'R', 'G', 'G', 'G'],
        5: ['G', 'R', 'G', 'G', 'G']
    }
        
    range_num = len(color_dict)

    result_dict = {'R': 0, 'G': 0, 'B': 0}

    color = ['R', 'G', 'B']
    
    color_list = padding_zero(range_num, color_dict)
    
    color_list_copy = copy.deepcopy(color_list)
    
    for i in color_list_copy:
        print(i)
    
    for c in ["R"]:
        color = Color(color_list_copy, h, w, c)
        color.target_color()