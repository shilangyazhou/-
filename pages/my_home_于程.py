'''主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('首页', ['关于根据地', '图片处理工具', '智能词典','自我介绍','留言区'])

def page_1():
    '''关于根据地'''
    st.write('# :sparkles: :blue[星迹]')
    st.write('根据地用途：工具分享、数据收集、兴趣推荐、综合主站')
    st.write('现有模块：图片处理工具、智慧词典、留言区')
    st.write('第五人格（魔怔')
    st.image('约约.jpg')
    
def page_2():
    '''图片处理工具'''
    st.write('# :sunglasses:图片换色程序:sunglasses')
    uploaded_file = st.file_uploader('上传图片',type=['png','jpng','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,1,0,2))
        with tab3:
            st.image(img_change(img,2,1,0))
        with tab4:
            st.image(img_change(img,0,1,2))
            
def page_3():
    '''智能词典'''
    st.write('# :green[智能词典]')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
            words_dict = {}
        for w in words_list:
            words_dict[w[1]] = [int(w[0]),w[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('Hello world')''')
        elif word == 'balloon':
            st.balloons()
        elif word == 'snow':
            st.snow()

def page_4():
    '''自我介绍'''
    st.write('# :blue[自我介绍]')
    st.write('关于我 emm...没什么好说的')
    st.write('第一，已自毁双目（可乐(bushi。。。）')
    st.write('第二，我推cp金婚：隐囚，摄殓，心患')
    st.write('第三，约推，摄厨（非癫厨')
    st.write('第四，祝你推红红火火，你推cp金婚')
    st.write(':orange[第五，人格启动（撕心裂肺音]')
    st.image('美约约.jpg')
    go = st.selectbox('选择想要跳转的网页', ['百度', '网易云音乐','哔哩哔哩'])
    if go == '百度':
        st.link_button('跳转到'+go,'https://www.baidu.com/')
    elif go == '网易云音乐':
        st.link_button('跳转到'+go,'https://music.163.com/')
    elif go == '哔哩哔哩':
        st.link_button('跳转到'+go,'https://www.bilibili.com/')

def page_5():
    '''留言区'''
    st.write('# :green[留言区]')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list = f.read().split('\n')
        for i in range(len(message_list)):
            message_list[i] = message_list[i].split('#')
        for i in message_list:
            if i[1] =='阿短':
                with st.chat_message('✨'):
                    st.write(i[1]+':'+i[2])
            elif i[1]=='编程猫':
                with st.chat_message('☕'):
                    st.text(i[1]+':'+i[2])
        name = st.selectbox('我是......',['阿短','编程猫'])
        new_message = st.text_input('想要说的话......')
        if st.button('留言'):
            message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] +'#' + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img,rc,gc,bc):
    '''图片处理工具'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img

if page == '关于根据地':
    page_1()
    
elif page == '图片处理工具':
    page_2()
    
elif page == '智能词典':
    page_3()
    
elif page == '自我介绍':
    page_4()

elif page == '留言区':
    page_5()
