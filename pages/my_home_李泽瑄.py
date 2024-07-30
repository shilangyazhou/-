import turtle
from PIL import Image

def page_1():
    st.write('### :blue[网络根据地]')
    st.write('#### 世界冒险')
    st.write('你喜欢去哪里冒险？')
    col5, col6 = st.columns([1, 1])
    with col5:
        cb1 = st.checkbox('A.去海边游泳')
        st.image('aduan_去海边游泳.png')
    with col6:
        cb2 = st.checkbox('B.去森林里露营')
        st.image('aduan_去森林里露营.png')
    col7, col8 = st.columns([1, 1])
    with col7:
        cb3 = st.checkbox('C.去沙漠看金字塔')
        st.image('aduan_去沙漠看金字塔.png')
    with col8:
        cb4 = st.checkbox('D.去雪山上滑雪')
        st.image('aduan_去雪山上滑雪.png')
    st.write(' ')
    st.write('你喜欢乘坐什么交通工具旅游？')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        cb1 = st.checkbox('A.汽车')
    with col2:
        cb2 = st.checkbox('B.高铁')
    with col3:
        cb3 = st.checkbox('C.飞机')
    with col4:
        cb4 = st.checkbox('D.渡轮')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        
def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 处理单词数据
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 构建新的数据结构
    words_dict = {}
    for w in words_list:
        words_dict[w[1]] = [int(w[0]),w[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for w in times_list:
        times_dict[w[0]] = int(w[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词:')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        st.write(f'### :blue[{words_dict[word][1]}]')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello,world')''')
        elif word == 'balloon':
            st.balloons()
        elif word == 'snow':
            st.snow()

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容， 并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1]+':'+i[2])
        elif i[1] == '编程猫':
            with st.chat_message('☔'):
                st.text(i[1]+':'+i[2])
    '''新增留言内容'''
    name = st.selectbox('我是……',['阿短','编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page_5():
    '''我的音乐'''
    type = st.radio('你最喜欢哪种风格的音乐？', ['流行', '嘻哈', '抒情', '民谣'],)
    if type == '流行':
        st.write('哇！我们有相同的喜好')
    else:
        st.write('很高兴与你分享音乐！')
    st.write('### :red[音乐时间！]')
    st.write('#### 我的最爱：')
    st.write('##### 《Lavender Haze》')    
    st.audio('Taylor Swift - Lavender Haze (Explicit).mp3')
    st.write('### 更多好听的音乐即将到来……')

#功能函数区
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    

'我的主页'

import streamlit as st


page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','我的音乐'])

'''
LEE的工作室\n
根据地用户：个人使用\n
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站\n
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区\n
原创模块：我的音乐\n
WELCOME TO MY SPACE:sunglasses:\n
'''

'我的兴趣推荐'

'我的图片处理工具'

'我的智能词典'

'我的留言区'

'我的音乐'

if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的智能词典') :
    page_3()
elif (page == '我的留言区') :
    page_4()
elif (page == '我的音乐') :
    page_5()
else :
    pass
