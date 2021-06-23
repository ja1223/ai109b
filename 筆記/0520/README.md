# 反傳遞演算法
反傳遞算法》的運作原理，則是建築在《微積分的鏈鎖規則》上，如以下算式所示：<br>
![](images/l.png)<br>
## 程式實作
[net1.py](net1.py)
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520>python net1.py
net.forward()= 10
net.backwward()
x= v:1 g:2 y= v:3 g:6 o= v:10 g:1
gfx = x.g/o.g =  2.0 gfy = y.g/o.g= 6.0
```
[net2.py](net2.py)
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520>python net2.py
0  =>  10
1  =>  9.216
2  =>  8.4934656
3  =>  7.827577896960003
4  =>  7.213895789838339
5  =>  6.648326359915014
6  =>  6.127097573297678
7  =>  5.646733123551139
8  =>  5.2040292466647315
9  =>  4.796033353726214
10  =>  4.42002433879408
11  =>  4.073494430632624
12  =>  3.754132467271026
13  =>  3.4598084818369785
14  =>  3.1885594968609583
15  =>  2.93857643230706
(中間省略)
86  =>  0.008925901352939013
87  =>  0.008226110686868595
88  =>  0.007581183609018099
89  =>  0.006986818814071082
90  =>  0.006439052219047909
91  =>  0.005934230525074554
92  =>  0.005468986851908708
93  =>  0.005040218282719065
94  =>  0.004645065169353892
95  =>  0.004280892060076547
96  =>  0.003945270122566546
97  =>  0.003635960944957329
98  =>  0.003350901606872675
99  =>  0.003088190920893857
x= 0.01687031935884968 y= 0.050610958076549  
```
## pytorch
PyTorch主要有兩大特徵：<br>
1. 類似於NumPy的張量計算，可使用GPU加速。
2. 基於帶自動微分系統的深度神經網路。
要使用pytorch需要先執行指令 : pip install torch<br>
利用pytorch自動微分的功能
[autograd0.py](autograd0.py)<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520>python autograd0.py
tensor(2.)
tensor(6.)
10.0   
```
[autograd1.py](autograd1.py)<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520python autograd1.py
tensor(2.)
tensor(6.)
10.0
```
[autograd2.py](autograd2.py)<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520python autograd2.py
f= 10.0
x.grad= tensor([2., 6.])
```
[torchGd1.py](torchGd1.py)只有單一參數<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520python torchGd1.py
99 x= 0.05263785645365715 loss= 3.792219400405884
199 x= 0.4059540331363678 loss= 2.540982484817505
299 x= 0.6951667666435242 loss= 1.702589750289917
399 x= 0.9319067597389221 loss= 1.1408231258392334
499 x= 1.1256942749023438 loss= 0.7644104957580566
599 x= 1.2843221426010132 loss= 0.5121946334838867
699 x= 1.4141700267791748 loss= 0.3431968688964844
799 x= 1.5204591751098633 loss= 0.22995948791503906
899 x= 1.6074634790420532 loss= 0.1540849208831787
999 x= 1.6786823272705078 loss= 0.10324501991271973
1099 x= 1.7369800806045532 loss= 0.06917953491210938
1199 x= 1.784700870513916 loss= 0.046353816986083984
1299 x= 1.8237634897232056 loss= 0.03105926513671875
1399 x= 1.8557382822036743 loss= 0.02081155776977539
1499 x= 1.881912112236023 loss= 0.013944864273071289
1599 x= 1.903337001800537 loss= 0.009343624114990234
1699 x= 1.9208747148513794 loss= 0.006260871887207031
1799 x= 1.93523108959198 loss= 0.004194974899291992
1899 x= 1.9469819068908691 loss= 0.002810955047607422
1999 x= 1.9566009044647217 loss= 0.0018835067749023438
2099 x= 1.9644749164581299 loss= 0.0012619495391845703
2199 x= 1.9709208011627197 loss= 0.0008456707000732422
2299 x= 1.9761968851089478 loss= 0.0005664825439453125
2399 x= 1.980515956878662 loss= 0.0003795623779296875
2499 x= 1.9840511083602905 loss= 0.0002543926239013672
2599 x= 1.9869447946548462 loss= 0.0001704692840576172
2699 x= 1.9893134832382202 loss= 0.00011420249938964844
2799 x= 1.9912525415420532 loss= 7.653236389160156e-05
2899 x= 1.9928398132324219 loss= 5.125999450683594e-05
2999 x= 1.9941390752792358 loss= 3.4332275390625e-05
3099 x= 1.9952024221420288 loss= 2.3126602172851562e-05
3199 x= 1.996072769165039 loss= 1.5497207641601562e-05
3299 x= 1.9967851638793945 loss= 1.0251998901367188e-05
3399 x= 1.997368574142456 loss= 6.9141387939453125e-06
3499 x= 1.9978458881378174 loss= 4.5299530029296875e-06
3599 x= 1.9982366561889648 loss= 3.0994415283203125e-06
3699 x= 1.9985564947128296 loss= 2.1457672119140625e-06
3799 x= 1.998818278312683 loss= 1.430511474609375e-06
3899 x= 1.999032735824585 loss= 9.5367431640625e-07
3999 x= 1.9992082118988037 loss= 7.152557373046875e-07
4099 x= 1.9993516206741333 loss= 4.76837158203125e-07
4199 x= 1.9994691610336304 loss= 2.384185791015625e-07
4299 x= 1.999565601348877 loss= 2.384185791015625e-07
4399 x= 1.9996439218521118 loss= 2.384185791015625e-07
4499 x= 1.9997082948684692 loss= 0.0      
4599 x= 1.9997607469558716 loss= 0.0      
4699 x= 1.9998042583465576 loss= 0.0      
4799 x= 1.9998400211334229 loss= 0.0      
4899 x= 1.999867558479309 loss= 0.0       
4999 x= 1.9998914003372192 loss= 0.0      
Result: x = 1.9998916387557983 loss=0.0 
```

[torchGd2.py](torchGd2.py)可以有多參數<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520>python torchGd2.py 
99 parameters= [tensor(0.3926, requires_grad=True)] loss= 2.583590269088745
199 parameters= [tensor(0.6843, requires_grad=True)] loss= 1.7311391830444336       
299 parameters= [tensor(0.9230, requires_grad=True)] loss= 1.1599531173706055       
399 parameters= [tensor(1.1184, requires_grad=True)] loss= 0.7772283554077148       
499 parameters= [tensor(1.2783, requires_grad=True)] loss= 0.520782470703125        
599 parameters= [tensor(1.4093, requires_grad=True)] loss= 0.3489518165588379       
699 parameters= [tensor(1.5165, requires_grad=True)] loss= 0.23381495475769043      
799 parameters= [tensor(1.6042, requires_grad=True)] loss= 0.15666794776916504      
899 parameters= [tensor(1.6760, requires_grad=True)] loss= 0.10497546195983887      
999 parameters= [tensor(1.7348, requires_grad=True)] loss= 0.07033920288085938      
1099 parameters= [tensor(1.7829, requires_grad=True)] loss= 0.04713082313537598     
1199 parameters= [tensor(1.8223, requires_grad=True)] loss= 0.031580209732055664    
1299 parameters= [tensor(1.8545, requires_grad=True)] loss= 0.021160364151000977    
1399 parameters= [tensor(1.8809, requires_grad=True)] loss= 0.01417851448059082     
1499 parameters= [tensor(1.9025, requires_grad=True)] loss= 0.009500265121459961    
1599 parameters= [tensor(1.9202, requires_grad=True)] loss= 0.006365776062011719    
1699 parameters= [tensor(1.9347, requires_grad=True)] loss= 0.004265308380126953    
1799 parameters= [tensor(1.9465, requires_grad=True)] loss= 0.0028579235076904297   
1899 parameters= [tensor(1.9562, requires_grad=True)] loss= 0.00191497802734375     
1999 parameters= [tensor(1.9642, requires_grad=True)] loss= 0.0012831687927246094   
2099 parameters= [tensor(1.9707, requires_grad=True)] loss= 0.0008597373962402344   
2199 parameters= [tensor(1.9760, requires_grad=True)] loss= 0.000576019287109375    
2299 parameters= [tensor(1.9804, requires_grad=True)] loss= 0.0003859996795654297   
2399 parameters= [tensor(1.9839, requires_grad=True)] loss= 0.0002586841583251953   
2499 parameters= [tensor(1.9868, requires_grad=True)] loss= 0.00017333030700683594  
2599 parameters= [tensor(1.9892, requires_grad=True)] loss= 0.00011610984802246094  
2699 parameters= [tensor(1.9912, requires_grad=True)] loss= 7.772445678710938e-05   
2799 parameters= [tensor(1.9928, requires_grad=True)] loss= 5.221366882324219e-05   
2899 parameters= [tensor(1.9941, requires_grad=True)] loss= 3.504753112792969e-05   
2999 parameters= [tensor(1.9952, requires_grad=True)] loss= 2.3365020751953125e-05  
3099 parameters= [tensor(1.9960, requires_grad=True)] loss= 1.5735626220703125e-05  
3199 parameters= [tensor(1.9968, requires_grad=True)] loss= 1.049041748046875e-05   
3299 parameters= [tensor(1.9973, requires_grad=True)] loss= 7.152557373046875e-06   
3399 parameters= [tensor(1.9978, requires_grad=True)] loss= 4.76837158203125e-06    
3499 parameters= [tensor(1.9982, requires_grad=True)] loss= 3.0994415283203125e-06  
3599 parameters= [tensor(1.9985, requires_grad=True)] loss= 2.1457672119140625e-06  
3699 parameters= [tensor(1.9988, requires_grad=True)] loss= 1.430511474609375e-06   
3799 parameters= [tensor(1.9990, requires_grad=True)] loss= 9.5367431640625e-07     
3899 parameters= [tensor(1.9992, requires_grad=True)] loss= 7.152557373046875e-07   
3999 parameters= [tensor(1.9993, requires_grad=True)] loss= 4.76837158203125e-07    
4099 parameters= [tensor(1.9995, requires_grad=True)] loss= 2.384185791015625e-07   
4199 parameters= [tensor(1.9996, requires_grad=True)] loss= 2.384185791015625e-07   
4299 parameters= [tensor(1.9996, requires_grad=True)] loss= 2.384185791015625e-07   
4399 parameters= [tensor(1.9997, requires_grad=True)] loss= 0.0
4499 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
4599 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
4699 parameters= [tensor(1.9998, requires_grad=True)] loss= 0.0
4799 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
4899 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
4999 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
Result: parameters = [tensor(1.9999, requires_grad=True)] loss=0.0
```

[torchGd3.py](torchGd3.py)直接求出最小值<br>
```
執行結果:
C:\Users\user\Desktop\ai\ai109b\筆記\0520python torchGd3.py
x= tensor([-0.0018, -0.0035], requires_grad=True)
```