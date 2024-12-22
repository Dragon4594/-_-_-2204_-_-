import random

class dr():
    type=0
    rasp= []
    in_dr = 0
    id_buss=0
    time_work = 0
    to=0
    def __init__(self,t,id,idb,a):
        self.type = t
        self.rasp = a
        self.id_dr = id
        self.id_buss = idb
        self.time_work = 0
        if t==0:
            self.to=60
        if t==1:
            self.to = 115
    def get_type(self):
        return self.type
    def get_rasp_drv(self):
        return self.rasp
    def get_drv_id(self):
        return self.id_dr
    def get_idb(self):
        return self.id_buss
    def get_time_w(self):
        return self.time_work
    def get(self):
        return 1
    def get_to(self):
        return self.to
    def set_tasp(self,a):
        self.rasp.append(a)
    def set_idb(self,idb):
        self.id_buss=idb
    def set_time_w(self,t):
         self.time_work=t

    def set_to(self):
        self.to = self.to - 1
    def set_toq(self):
        if  self.type==0 and self.to-1!=-1:
            self.to=self.to-1
        if self.type==1 and self.to-1!=99 and self.to-1!=83 and self.to-1!=43 and self.to-1!=28 and self.to-1!=13 and self.to-1!=-2:
            self.to = self.to - 1




class buss():
    id_bus=0
    rasp_b=[]
    time=0
    dr_in = 0
    t2=0
    t=0
    def __init__(self,idb,t,a,d):
        self.id_bus=idb
        self.rasp_b=[a]
        self.time=t
        self.dr_in = d
        self.t2=t
        self.t=0
    def get_t2(self):
        return self.t2
    def get_id_bus(self):
        return self.id_bus
    def get_rasp_b(self):
        return self.rasp_b
    def get_time(self):
        return self.time
    def get_drin(self):
        return self.dr_in
    def get_t(self):
        return self.t
    def set_rasp_b(self,a):
        self.rasp_b.append(a)

    def set_mtime(self, t):
        self.time = t
    def set_time(self,t):
        if (self.dr_in > 0):
            if (self.time-1!=0):
                self.time=t
    def set_drin(self,a):
        self.dr_in=a
    def set_t2(self,t):
        self.t2=t
    def set_t(self,a):
        self.t=a
    def marshend(self):
        if self.t2<=0:
            self.t2=random.randint(50, 70)
            self.t=1

def num(a,id):
    for i in range(8):
        if a[i].get_drin()==id:
            return i
    return 0



def rasp():

    rs=[]
    for z in range (8):
        if z==0:
            rs.append([])
            for i in range(1,9):
                if i==0:
                    rs[z].append(buss(i,60,[i,360],1))
                else:
                    rs[z].append(buss(i, 0, [], 0))
            for i in range(9,25):
                if (i==9):
                    rs[z].append(dr(random.randint(0, 1), i-8, 1, [1,360]))
                else:
                    rs[z].append(dr(random.randint(0, 1), i - 8, 0, []))
        else:
            rs.append([])
            for i in range(1,24):

                if i <9:
                    if i==1:
                        rs[z].append(buss(i, 60, [i,360], 1))
                    else:
                        rs[z].append(buss(i,0,[],0))
                else:
                    if i==9:
                        rs[z].append(dr(rs[0][i].get_type(),i-8,rs[0][i].get_idb(),rs[0][i].get_rasp_drv()))
                    else:

                        rs[z].append(dr(rs[0][i].get_type(), i - 8, 0, []))


    for z in range (8):

    # i рабочий день маршрута с 6 утра по 3 часа ночи т.е 21 час или 1260 мин и 7-9 часы пик это 60-(60*3) в программе
        for i in range (360,1260+360):
            for n in range(23):
                    if n<8:
                        if rs[z][n].get_drin()!=0:
                            o=rs[z][n].get_time()
                            rs[z][n].set_time(o-1)
                            if(rs[z][n].get_t2()>0):
                                rs[z][n].set_t2(rs[z][n].get_t2()-1)
                            else:
                                rs[z][n].marshend()

                    else:
                        #нужно сделать проверку на то что отдыхает вожитель сейчас или нет в зависимоти от этого крутить счетчик работы/отдыха
                        if (rs[z][n].get_idb()!=0):
                            rs[z][n].set_time_w(rs[z][n].get_time_w()+1)
                            #8 часов + перерыв 60 мин
                            if (rs[z][n].get_type()==0):
                                if rs[z][n].get_time_w()>120 and (rs[z][n].get_to()==60):
                                    if (not ((i>=60) and  (i<60*3)) and not((i<=11*60) and (i>13*60))) and (rs[z][num(rs[z],n)].get_time()==1) and (rs[z][num(rs[z],n)].get_t()==1):
                                        #поиск свободного водителя в парке
                                        for tt in range(9,23):
                                            #добавить переменную отработал ли сегодня полностью
                                            if (rs[z][tt].get_idb()==0) and (rs[z][tt].get_to()>0):
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_t(0)
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_time(60)
                                                #rs[z][num(rs[z], rs[z][n].get_idb())].set
                                                rs[z][tt].set_tasp(num(rs[z], rs[z][n].get_idb()))
                                                rs[z][tt].set_tasp(i)
                                                rs[z][tt].set_idb(rs[z][num(rs[z], rs[z][n].get_idb())].get_id_bus())

                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_drin(tt-8)#в скобочках номер водителя нового рандомного
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_rasp_b([tt-8,i])

                                                break

                                        # если не нашли берём рандомного

                                        rs[z][n].set_idb(0)
                                        rs[z][n].set_tasp(i)
                            else:
                                if rs[z][n].get_time_w()>120 and (rs[z][n].get_to()>0):
                                    if (not ((i>=60) and  (i<60*3)) and not((i<=11*60) and (i>13*60))) and (rs[z][num(rs[z],n)].get_time()==1) and (rs[z][num(rs[z],n)].get_t()==1):
                                        #поиск свободного водителя в парке
                                        for tt in range(9,23):
                                            #добавить переменную отработал ли сегодня полностью
                                            if (rs[z][tt].get_idb()==0) and (rs[z][tt].get_to()>0):
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_t(0)
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_time(60)
                                                #rs[z][num(rs[z], rs[z][n].get_idb())].set
                                                rs[z][tt].set_tasp(num(rs[z], rs[z][n].get_idb()))
                                                rs[z][tt].set_tasp(i)
                                                rs[z][tt].set_idb(rs[z][num(rs[z], rs[z][n].get_idb())].get_id_bus())

                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_drin(tt-8)#в скобочках номер водителя нового рандомного
                                                rs[z][num(rs[z], rs[z][n].get_idb())].set_rasp_b([tt-8,i])

                                                break

                                        # если не нашли берём рандомного

                                        rs[z][n].set_idb(0)
                                        rs[z][n].set_tasp(i)
                        else:
                            if (rs[z][n].get_type()==0):
                                rs[z][n].set_toq()
                                if rs[z][n].get_to()==0:
                                    for tt in range(8):
                                        if(rs[z][tt].get_drin()==0):
                                            rs[z][n].set_idb(rs[z][tt].get_id_bus())
                                            rs[z][n].set_tasp(rs[z][tt].get_id_bus())
                                            rs[z][n].set_tasp(i)
                                            rs[z][tt].set_time(random.randint(50,70))
                                            rs[z][tt].set_t2(rs[z][tt].get_time())
                                            rs[z][tt].set_drin(rs[z][n].get_drv_id())
                                            rs[z][tt].set_rasp_b([rs[z][n].get_drv_id(),i])
                            if (rs[z][n].get_type() == 1):
                                rs[z][n].set_toq()
                                if rs[z][n].get_to()-1==99 or rs[z][n].get_to()-1==83 or rs[z][n].get_to()-1==43 or rs[z][n].get_to()-1==28 or rs[z][n].get_to()-1==13 or rs[z][n].get_to()-1==-2:
                                    for tt in range(8):
                                        if(rs[z][tt].get_drin()==0):
                                            rs[z][n].set_idb(rs[z][tt].get_id_bus())
                                            rs[z][n].set_tasp(rs[z][tt].get_id_bus())
                                            rs[z][n].set_tasp(i)
                                            rs[z][tt].set_time(random.randint(50,70))
                                            rs[z][tt].set_t2(rs[z][tt].get_time())
                                            rs[z][tt].set_drin(rs[z][n].get_drv_id())
                                            rs[z][tt].set_rasp_b([rs[z][n].get_drv_id(),i])
    return rs
a=rasp()
for i in range(1,len(a)):
    print("dey", i )
    for t in range(8,23):
        print(a[i][t].get_drv_id(),' ',a[i][t].get_type())
        print(a[i][t].get_rasp_drv())

