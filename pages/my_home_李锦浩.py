'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','凡尘神域'])
import time
"""
工作室名字：守夜人 夜幕
根据地用户：个人使用、只有几个人知道的秘密基地、分享后所有人可见……
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感：……
原创模块：……
原创模块一句话功能介绍：……
"""
def page_1():
    '''我的兴趣推荐'''
    st.write('###### :purple[导语:你是否想过，在霓虹璀璨的都市之下，潜藏着来自古老神话的怪物？你是否想过，在那高悬于世人头顶的月亮之上，伫立着守望人间的神明？你是否想过，在人潮汹涌的现代城市之中，存在代替神明行走人间的 超凡之人？人类统治的社会中，潜伏着无数诡异；在那些无人问津的生命禁区，居住着古老的神明。炽天使米迦勒，冥王哈迪斯，海神波塞冬……而属于大夏的神明，究竟去了何处？在这属于“人”的世界，“神秘”需要被肃清！]')
    st.write('# :blue[《我在精神病院学斩神》]')
    st.write('#### :gold[作者:三九音域]')
    st.image('屏幕截图 2024-07-20 213204.png')
    st.write('### :red[大夏境内，神明禁行]')
    st.image('aduan_天象奇景.jpg')
    st.audio('霞光.mp3')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img_change(img,1,0,2))
        with tab1:
            st.image(img_change(img,2,0,1))
        with tab1:
            st.image(img_change(img,1,2,0))
        with tab1:
            st.image(img_change(img,1,1,1))
def page_3():
    '''我的智能词典'''
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    print(words_list)
    print("-"*100)
    
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    print(words_list)
    print("-"*100)
    
    words_dict = {}
    for w in words_list:
        words_dict[w[1]] = [int(w[0]),w[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")    
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word =st.text_input('请输入要查询的单词')

    if word in words_dict:
        st.write(words_dict[word])
    if word == "night":
        st.snow()
        st.write('###### :blue[恭喜你触发彩蛋！]')
def page_4():
    '''我的留言区'''
    st.write('评论区')
    with open("leave_messages.txt",'r',encoding='utf-8') as f:            
        messages_list = f.read().split('\n')   
    for i in range(len(messages_list)):
        messages_list[i] =messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('👾'):
                st.write(i[1]+':'+i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🤖'):
                st.write(i[1]+':'+i[2])
    name = st.selectbox('我是……',['阿短','编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:    
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message=message[:-1]
            f.write(message)

def page_5():
    '''凡尘神域'''
    st.write('##### :blue[若黯夜终临，吾必立于万万人之前，横刀向渊，血染天穹]')
    
    
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”!')
            st.balloons()
    st.write('下面哪些小程序可以被嵌入网页中？')
    cb1 = st.checkbox('A.turtle绘图作品')
    cb2 = st.checkbox('B.图片处理工具')
    cb3 = st.checkbox('C.智能词典工具')
    cb4 = st.checkbox('D.pygame小游戏')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            st.write('回答正确！')
            st.snow()
            st.link_button('视频','https://www.bilibili.com/video/BV1sN411y7mX/?share_source=copy_web')
        else:
            st.write('再想想')

def img_change(img,rc,gc,bc):
    width,height=img.size
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
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '凡尘神域':
    page_5()
