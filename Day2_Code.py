with open(r'C:\AOC\Day2_Input.txt', encoding='utf-8') as input_file:
    paper = 0
    ribbon = 0
    for current_line in iter(input_file.readline, ''):
        ribbon_wrap = 0
        perimetr  = 0
        nums_on_line = current_line.split(r'x')
        nums_on_line = list(map(int, nums_on_line))
        length,width,height = nums_on_line[0:3]
        side_no1 = length * width
        side_no2 = width * height
        side_no3 = height * length
        add_paper = min(side_no1,side_no2,side_no3)
        max_var = max(nums_on_line)
        nums_on_line.remove(max_var)
        ribbon_bow = nums_on_line
        ribbon_wrap = 2 * ribbon_bow[0] + 2 * ribbon_bow[1]
        ribbon_wrap += length * width * height
        perimetr = 2*side_no1 + 2*side_no2 + 2*side_no3 + add_paper
        paper += perimetr
        ribbon += ribbon_wrap
    result = (paper,ribbon)
with open(r'C:\AOC\Day2_Output.log', mode='w', encoding='utf-8') as output_file:
        output_file.write(str(result))
