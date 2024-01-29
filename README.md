این برنامه از الگوریتم (LCG (linear congruential generator برای تولید دنباله اعداد Pseudorandom بهره میگرد.
برای دسترسی به ماژول LCG:
```
num = LCG(seed=) #default seed is time.time()
print(num.normal_genarator(mean,variance))
print(num.int_generator([a,b])) #sample num.int_generator([lower_bound , upper bound]) #upper bound not included
print(num.float_generator([a,b] , d))#d تعداد رقم بعد از اعشار است که قابل شخصی سازیست
```
