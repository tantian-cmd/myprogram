#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�̸��2019.11.16
"""

import random
comp_number=random.randrange(0,5)
player_choice_number=100

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(player_choice): 
    global player_choice_number
    if player_choice=="ʯͷ":
        player_choice_number=0
    elif player_choice=="ʷ����":
        player_choice_number=1
    elif player_choice=="ֽ":
        player_choice_number=2
    elif player_choice=="����":
        player_choice_number=3
    elif player_choice=="����":
        player_choice_number=4
    else:
        print("Error: No Correct Name")
    return player_choice_number

        
"""
����Ϸ�����Ӧ����ͬ������
"""
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


     #��дִ�д���,������ɺ�passɾ��


def number_to_name(comp_number):
    if comp_number==0:
        name="ʯͷ"
    elif comp_number==1:
        name="ʷ����"
    elif comp_number==2:
        name="ֽ"
    elif comp_number==3:
        name="����"
    elif comp_number==4:
        name="����"
    print("�������ѡ����:"+name)
    return name
"""
������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
"""

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice_number,comp_number):
    if  player_choice_number==0 and comp_number==3:
        print("��Ӯ��")
    elif player_choice_number==0 and comp_number==4:
        print("��Ӯ��")
    elif player_choice_number==1 and comp_number==0:
        print("��Ӯ��")
    elif player_choice_number==1 and comp_number==4:
        print("��Ӯ��")
    elif player_choice_number==2 and comp_number==0:
        print("��Ӯ��")
    elif player_choice_number==2 and comp_number==1:
        print("��Ӯ��")
    elif player_choice_number==3 and comp_number==1:
        print("��Ӯ��")
    elif player_choice_number==3 and comp_number==1:
        print("��Ӯ��")
    elif player_choice_number==4 and comp_number==2:
        print("��Ӯ��")
    elif player_choice_number==4 and comp_number==3:
        print("��Ӯ��")
    elif player_choice_number==comp_number:
        print("���ͼ����ѡ���һ��")
    else:
        print("�����Ӯ��")
    
    
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
print("-----")
print("����ѡ����:"+player_choice)
name_to_number(player_choice)
number_to_name(comp_number)
rpsls(player_choice_number,comp_number)



