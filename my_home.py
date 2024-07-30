'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '游戏小调查','音乐推荐','我的图片处理工具', '我的智能词典', '我的留言区','关于此网站'])
info="""
工作室名字：龙哥工作室\n
根据地用户：分享后所有人可见\n
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站\n
"""
def page_1():
    '''我的兴趣推荐'''
    # st.write('----')
    w1, w2 = st.columns([1, 1])
    with w1:
        cb1 = st.write("## :red[化学]")
    with w2:
        cb2 = st.image('原子.jpg')
    st.write("##### 化学既神秘又充满魅力,每一个原子虽渺小但蕴含力量\n ##### 它是沟通微观与宏观物质世界的重要桥梁，也是人类认识和改造物质世界的主要方法和手段之一.....")
    st.write("\n ### 合成材料")
    st.write("###### 复合材料是随着材料化学等科学技术进步而发展起来的一种新兴材料,\n ###### 复合材料具有质轻、强度高、耐磨等优点,广泛地用于航空、化工、电气制造等行业")
    st.image('合成材料.jpg')
    st.write('----')
    st.write("\n ### 核工业")
    st.write("###### 核工业是一门学科门类多、开拓领域广、技术密集程度高的综合性新兴工业,涉及物理、化学、电子学、半导体、计算机技术、材料学、传热学和生物学等学科领域\n ###### 核工业是从事核燃料研究、生产、加工，核能开发、利用，核武器研制、生产的工业,在国民经济发展中，核工业具有极为重要的地位和作用")
    p1, p2 = st.columns([1, 1])
    with p1:
        cb3 = st.image('核2.jpg')
    with p2:
        cb4 = st.image('核1.jpg')
    # st.image('核1.jpg')
    # st.image('核2.jpg')
    # st.write("霞光")
    # st.audio('霞光.mp3')
        
def page_2():
    st.write('###### 下面我们来做一个小调查，\n ###### 请在你感兴趣的游戏类型前勾选,我会顺带依据你选择的类型来推荐我喜欢的游戏')
    st.write('----')
    cb1 = st.checkbox('沙盒、生存类游戏')
    cb2 = st.checkbox('动作射击类游戏')
    cb3 = st.checkbox('动作冒险类游戏')
    cb4 = st.checkbox('音乐类游戏')
    cb5 = st.checkbox('竞速类游戏')
    cb6 = st.checkbox("其他类")
    l = [cb1, cb2, cb3, cb4, cb5, cb6]
    if st.button("确认提交"):
        if True in l:
            st.write(":blue[提交成功!]")
        else:
            st.write(":red[提交失败，请填写内容！]")
    if cb1:
        st.write('##### 推荐《Terraria》、《GMod》、《饥荒》、《方舟：生存进化》')
    if cb2:
        st.write('##### 推荐《CSGO》、《求生之路2》、《辐射4》、《战地风云系列》、《汤姆克兰西系列》')
    if cb3:
        st.write('##### 推荐《荒野大镖客2》、《只狼：影逝二度》、《合金装备系列》、《古墓丽影系列》')
    if cb4:
        st.write('##### 推荐《冰与火之舞》(哈哈哈)、《Phigros》')
    if cb5:
        st.write('##### 推荐《极限竞速：地平线5》')

    i1, i2, i3, i5, i4 = st.columns([1, 1, 1, 1, 1])
    with i1:
        if l[0]:
            cd1 = st.image('cb1.jpg')
    with i2:
        if l[1]:
            cd2 = st.image('cb2.jpg')
    with i3:
        if l[2]:
            cd3 = st.image('cb3.jpg')
    with i4:
        if l[3]:
            cd4 = st.image('cb4.png')
    with i5:
        if l[4]:
            cd5 = st.image('cb5.jpg')
    
    
def page_3():
    st.write("#### :blue[这是一些我个人喜爱的音乐，与你们分享]")
    st.write('### :blue[♪♪♪]')
    st.write('----')
    st.image('mpi1.jpg')
    st.write('###### Meg Myers - Running Up That Hill')
    st.audio('Running_Up_That_Hill.mp3')
    st.write('----')
    st.image('mpi2.jpg')
    st.write('###### Golubye Berety - Ekh, Dolya')
    st.audio('Ekh_Dolya.mp3')
    st.write('----')
    st.image('mpi3.jpg')
    st.write('###### Lube - Луговая трава')
    st.audio('Lube.mp3')
    st.write('#### 常用音乐网站↓↓↓')
    st.link_button('网易云', 'https://music.163.com/')
    st.link_button('酷狗', '//www.kugou.com/')
    st.link_button('抠抠音乐', 'https://y.qq.com/')
    

def page_4():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,1,2))
        st.image(img_change(img,1,0,2))
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img_change(img,1,0,2))
        with tab2:
            st.image(img_change(img,2,1,2))
        with tab3:
            st.image(img_change(img,2,2,2))
        with tab4:
            st.image(img_change(img,0,1,2))
    st.write('----')
    st.write('什么，花里胡哨?那就试试这个图片处理网站，各种方法，免费使用......↓↓↓')
    st.link_button('iloveimg', 'https://www.iloveimg.com/zh-cn')
        

def page_5():
    '''我的智能词典'''
    st.write('智能词典')
    # 读取文本数据
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    #处理单词
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    #单词查询次数
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #将列表转换成字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_dict:
        times_dict[int(i[0])] = int(i[1])
        
    #创建输入框
    word = st.text_input("请输入要查询的单词")
    #显示查询内容
    if word in words_dict: 
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1 
        st.write('查询次数:',times_dict[n])
        st.write(f'### :blue[{words_dict[word][1]}]')
        
        
    # #输入框
    # word = st.text_input("请输入要查询的单词")
    # '''更新查询次数信息至txt文件'''
    with open('check_out_times.txt','w',encoding='utf-8') as f:
        message = ''
        for k,v in times_dict.items():
            message += str(k) + '#' + str(v) + '\n'
        message = message[:-1]
        f.write(message)

def page_6():
    '''我的留言区'''
    st.write('我的留言区')
    #加载内容
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
        
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('☀'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('☋'):
                st.write(i[1],':',i[2])
        elif i[1] == '普通路人':
            with st.chat_message('♟'):
                st.write(i[1],':',i[2])  

    name = st.selectbox('我是......',['阿短','编程猫','普通路人'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page_7():
    st.write(info)
    
#-----------------------功能函数-------------------------
def img_change(img,rc,gc,bc):
        '''图片处理'''
        width,height = img.size
        img_array = img.load()
        for x in range(width):
            for y in range(height):
                r = img_array[x,y][rc]
                g = img_array[x,y][gc]
                b = img_array[x,y][bc]
                img_array[x,y] = (b,g,r)
        return img
    
if page == '我的兴趣推荐':
    page_1()
elif page == '游戏小调查':
    page_2()
elif page == '音乐推荐':
    page_3()
elif page == '我的图片处理工具':
    page_4()
elif page == '我的智能词典':
    page_5()
elif page == '我的留言区':
    page_6()
elif page == '关于此网站':
    page_7()