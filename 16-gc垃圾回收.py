16 gc垃圾回收

程序运行过程中产生的垃圾占用着内存。


	避免垃圾产生的办法：

		1、小正数对象池：
			Python对小整数的定义是 [-5, 256] 的对象是'提前建立'好的。不会被垃圾回收。常驻内存。 
			即：
				a=100
				b=100
				c=100
				id(a)、id(b)、id(c)输出都是同样的，在内存中已经预先建立好，
			但是当超过上面的数值时，会重新建立对象。
			
			池的意思是说，已经缓存好，把所有东西准备在这里。


		2、大整数对象池：
		3、intern机制：字符串、整数类型，非可变类型，所以在内存中，相同的共用一份地址。
			简单无标点符号的共享，若有标点符号或者空格的则有一个新建一个。


Garbage collection(GC垃圾回收)：
	一个对象什么时候会被删除？
		引用计数为零的时候。

	什么时候会给这个引用计数+1？
		·对象被创建，例如a=23
		·对象被引用，例如b=a
		·对象被作为参数，传入到一个函数中，例如func(a)
		·对象作为一个元素，存储在容器中，例如list1=[a,a]
	
	什么时候引用计数-1？
		·对象的别名被显式销毁，例如del a
		·对象的别名被赋予新的对象，例如a=24
		·一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
		·对象所在的容器被销毁，或从容器中删除对象
	
	如何查看一个对象的引用计数？
		import sys
		a = "hello world"
		sys.getrefcount(a)  # 用这个数减去1是真正的引用数目，因为这个函数调用这个参数意识一次引用。



一、引用计数是Python中解决垃圾回收的机制之一。
	引用计数能解决大部分的情况，但是对如下情况无法解决：
		class ClassA():
			def __init__(self):
				print('object born,id:%s' % str(hex(id(self))))

		def f2():
			while True:
				c1 = ClassA()
				c2 = ClassA()
				c1.t = c2
				c2.t = c1
				del c1
				del c2
		f2()
		此时虽然c1,c2删除了，但是其内部还有t还在指向两个已经不应该存在的对象，类似双向链表。
		如果此时循环，则一直循环建立对象，始终删不掉。所以引用计数机制不能解决循环引用问题。

二、隔代/分代回收：
		import gc
		class ClassA():
			def __init__(self):
				print('object born,id:%s' % str(hex(id(self))))

		def f2():
			while True:
				c1 = ClassA()
				c2 = ClassA()
				c1.t = c2
				c2.t = c1
				del c1
				del c2
		gc.disable() #开关gx功能。或者显示的开启：手动执行垃圾回收gc.collection()
		f2()
		gx.Garbage打印清理垃圾对象信息。

创造一个链表，新建一个对象之后，就会挂靠在链表上，每一个引用计数加1，删除减1，如果出现循环引用的情况，此时引用数为1，
解决方案：每间隔一段时间或次数，触发链表检测：
	检测方式：
		查看对象之间是否存在相互引用，如果存在相互引用，那么所有循环引用的链子上的对象引用减去1，
		如果减1后为零，则收集器释放为零的对象并将内存空间回收，将非零的对象，新建一条链子，重新挂上去。


python中GC垃圾回收有两种机制：
	引用计数为主！ 隔代回收为辅





gc模块
	import gc
	
	gc.get_threshold()  
	返回值:(700,10,10)  
		如果新建的对象数量，减去已清理的对象数量，结果大于这个700（残留个数），则启动链表检测机制清理0代链表。
		每清理10次零代，清理一次零代和一代。
		每清理10次一代，清理一次零代、一代和二代。全部。

	gc.get_count()
	返回值：（581,5,3）
		获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表

	gc.set_threshold(threshold0[, threshold1[, threshold2]) 设置自动执行垃圾回收的频率。


	gc模块方法，依然有一个漏洞，就是在定义类的时候重写了__del__方法。
		因为类中__del__方法，就是在空间回收时gc类调用该类中的__del__方法，如果重写了，那将导致无法删除。此时无法清理。







