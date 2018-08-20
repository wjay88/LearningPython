多任务-进程


1、概念认知：
	实现方式:
	1）进程：
	2）线程：
	3）协程：

	Linux和windows都是多任务的，但是linux支持多用户同时登陆，windows不支持多用户同时登陆。

	单核：操作系统轮流让各个任务交替执行   		
	操作系统两种方式:
		时间片轮转。雨露均沾。
		优先级调度。

	多核：操作系统把很多任务轮轮流调度到每个核心上执行


	并发：看上去一起执行。		任务数量大于核数。
	并行：真正的一起执行。

	调度算法：
		什么样的情况下：按照什么样子的规则：让谁去执行。



2、在Python中多任务的实现：
	编写完毕的代码，在没有运行的时候，称之为 程序
	正在运行着的代码，就成为 进程
		程序是没有生命的，而进程是有生命的。
	进程，除了包含代码以外，还有需要运行的环境等，所以和程序是有区别的。


	python中使用fork()就能创建新的进程来。完成多任务的创建。
	    # 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以!!!!!!!

	首先导入os模块：
	import os

	ret = os.fork()
	fork()有两个返回值，特殊的。分两次返回。一次一个。fork()的功能，能创建一个新的进程。

	import os 
	import time
	ret = os.fork()    # 代码执行等号右边，fork()就会创建一个新的进程。新的进程也从此处开始执行。
	# 首先两个进程都会去完成左边的赋值。但是第一个进程父进程返回值大于零，第二个进程返回值等于零。
	# 所以说fork返回两个值。
	# 所以多任务最核心的就是有多个进程：多个进程的生成方式：fork().
	# fork()执行的时候，就会将代码复制一份生成一个子进程。
	# 操作系统为了区分子进程和父进程：让父进程返回值大于零，让子进程返回值等于零。
	print(ret)
	if ret ==0:
		while True:
			print('---1---')
			time.sleep(1)
	else:
		while True:
			print('---2---')
			time.sleep(2)
	# 根据返回值不同，执行不同的代码：
	# 同样是以上的代码：不同的机器，不同的环境执行情况不同：原因在于操作系统的调度算法不同：
	# 父进程创建的子进程，并无必然的先后顺序。
	os.fork()下面的代码父子进程都做。只不过是:通过if来分流。

	通过print(ret)会发现：
	父进程中fork的返回值，就是刚刚创建出来的子进程的pid。
		import os
		ret = os.fork()
		print(ret)
		if ret > 0:
		    print('---父进程---%d' % os.getpid())
		else:
		    print('---子进程---%d-%d' % (os.getpid(), os.getppid()))

	输出结果：
		5075
		---父进程---5074
		0
		---子进程---5075-5074

	进程本质就是fork返回值多个，通过if分流来实现并行执行。
	子进程永远返回0，而父进程返回子进程的ID。

	如果父子进程之间进度无关。各自为战，谁先结束都可以。无明显先后顺序。但是可以人为干预：time.sleep(0.5)
		import os
		import time

		ret = os.fork()

		if ret == 0:
		    print('---子进程1---over')
		    time.sleep(0.0001)
		    print('---子进程2---over')
		    time.sleep(0.0001)
		    print('---子进程3---over')
		    time.sleep(0.0001)
		    print('---子进程4---over')
		    time.sleep(0.0001)
		    print('---子进程5---over')

		else:
		    print('---父进程1---')
		    time.sleep(0.0001)
		    print('---父进程2---')
		    time.sleep(0.0001)
		    print('---父进程3---')
		    time.sleep(0.0001)
		    print('---父进程4---')
		    time.sleep(0.0001)
		    print('---父进程5---')
	
		输出情况：
		---父进程1---
		---子进程1---over
		---父进程2---
		---父进程3---
		---子进程2---over
		---子进程3---over
		---父进程4---
		---子进程4---over
		---父进程5---
		---子进程5---over





	全局变量在多个进程中不共享：进程之间数据不共享！！！解决办法：进程之间的通信。
		import os
		imort time

		g_num = 100
		
		ret = os.fork()
		if ret == 0:
			print('--process-1---')
			g_num += 1
			print('--process-1 g_num=%d' % g_num)
		else:
			time.sleep(0.5)
			print('--process-2-- g_num=%d' % g_num)
		输出情况：
		--process-1---
		--process-1 g_num=101
		--process-2-- g_num=100
	各自为战，fork之后，复制一份代码：独自运行，互不干扰。

	进程间的通信：可以在一台机器上，可以不在一台机器上。
		在一台机器上：管道，命名管道；消息队列。文件读取。
		不在一台机器上的：网络：网络就是进程之间通信做到的事情。



3、多个fork的情况：

	二叉树形式:执行。

		import os
		ret = os.fork()
		if ret == 0:
		    print('--process-1---')
		else:
		    print('--process-2---')

		ret = os.fork()
		if ret == 0:
		    print('--process-11---')
		else:
		    print('--process-22---')
	输出结果：
		--process-2---
		--process-22---
		--process-11---
		--process-1---
		--process-22---
		--process-11---



	下面是 fork()炸弹。
		while True:
			os.fork()


4、在windows下多任务python：Process类。可以跨平台！！！！！！

	Process类创建子进程：
		from multiprocessing import Process
		import time

		def test():
			while True:
				print('----test----')
				time.sleep(0.5)
		p = Process(target = test)
		p.start() # 让这个进程开始执行test函数里的代码。

		while True:
			print('---main---')
			time.sleep(1)
	这样就能实现多任务：
	核心以下两句：
		p = Process(target = test)  # 新建一个类对象。
		p.start()  # 让这个进程开始执行test函数里的代码。
		创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动。

	通过应用Process类创建子进程完成多任务可以实现跨平台！！！！
	而且	对比fork不同：
		主进程等待Process子进程先结束。
		主进程等待所有子进程over，主进程才over。

	join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
	堵塞：主进程运行到join（）这句，等待某种条件的发生的，才能继续执行，但是此时条件一直不发生，就会发生堵塞。
	解堵塞：等到条件发生，就继续执行。


5、升级版的创建子进程的方式:重新定义进程类：
	from multiprocessing import Process
	import time

	class MyNewProcess(Process):
		def run(self):
			while True:
				print('----1----')
				time.sleep(1)

	p = MyNewProcess()
	p.start()

	while True:
		print('---main---')
		time.sleep(1)

	重新定义的进程类，继承于Process。重新写了run方法。在启动p.start()的时候，会调用父类中的start方法，
	父类中的start方法，会自动执行新类中的方法。所以我们外部没有调用run的情况下也会执行。
	并非是我们主动调用的，而是start()方法会自动调用。

	类似：编程模式中的工程模式：父类中定义，子类中直接继承。
	
	time.ctime():返回字符串类型的时间。



6、创建子进程的另一种方式：进程池Pool
	from multiprocessing import Pool

	能用这种就用这种。

	池的作用就是缓存：

	from multiprocessing import Pool
	import os
	import random
	import time


	def worker(num):
	    for i in range(random.randint(1, 3)):
	        print('---pid--- = %d---num=%d---' % (os.getpid(),num))
	        time.sleep(1)

	pool = Pool(3)  # 进程池创建3个进程，准备工作。自动创建，节省了我们创建进程池，且实现自动销毁。

	for i in range(10):
	    print('---%d---' % i)
	    # 向进程池中添加任务
	    # 注意：如果添加的任务数量超过了 进程池中进程的个数的话，那么不会导致添加不进去。
	    # 添加到进程中的任务，如果还没有被执行的话，那么此时他们会等待进程池中的进程完成一个任务后，
	    # 会自动去用刚刚结束任务的进程来执行当前的新任务。
	    pool.apply_async(worker, (i,))

	pool.close()   # 进程池关闭之后，就不能再添加任务。
	pool.join()    # 等待某个进程结束。此处等待进程池内部所有任务完成。。
	               # 主进程 创建/添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束。
	               # 而是 当主进程的任务做完之后 立马结束， 如果这个地方没有join，会导致进程池中的任务不执行。


7、总结多种多任务新建进程方式:

	方式一：少用：
		ret = os.fork()
		if ret==0:
			子进程：
		else:
			父进程---
	方式二：
		p1 = Process(target =xxx,(xx,))
		p1.start()

	方式三：推荐：
		pool=Pool(3)   此处的数：完成压力测试可用。
		pool.apply_async(xxx,(xx,))
		# 主进程一般用来等待，真正的任务都在子进程中执行。


8、针对Pool中实现执行任务的方式:
	非堵塞的方式:Pool.apply_async()：添加完再添加，不管干完不干完。
	堵塞方式：Pool.apply()	执行完一个任务，在执行另一个。不完不干。此种情况几乎不用。

9、进程间的通信：Queue		消息队列

	进程的好处是：多任务，
			不足：数据文件不共享。

	进程间数据交互：Queue:队列：
		队列特点：先进先出：

		from multiprocessing import Queue
		q = Queue()
		q.get()
		q.put()
		q.get_nowait()
		q.empty()
		q.full()
		消息队列的给与取。

	代码：	
		from multiprocessing import Process,Queue
		import os
		import random
		import time


		def write(q):
		    for value in ['A', 'B', 'C']:
		        print('put %s to queue...' % value)
		        print('进程编号pid=%d' % os.getpid())
		        q.put(value)
		        time.sleep(random.random())


		def read(q):
		    while True:
		        if not q.empty():
		            value = q.get(True)
		            print('get %s from queue' % value)
		            print('进程编号pid=%d' % os.getpid())
		            time.sleep(random.random())
		        else:
		            break

		if __name__=='__main__':
		    q = Queue()
		    pw = Process(target=write, args=(q,))
		    pr = Process(target=read, args=(q,))

		    pw.start()
		    pw.join()

		    pr.start()
		    pr.join()

		    print('')
		    print('所有数据已写入并且读取完毕！')







10、进程池中的Queue：
	如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，
	而不是multiprocessing.Queue()，

	方式：

		q1 = Manager().Queue()  # 只有此处：不同：
		po = Pool()

		po.apply(write,(q1,))
		po.apply(reader,(q1,))




11、多进程拷贝文件：
	copyFiles.py


	import os
	from multiprocessing import Pool, Manager
	import time


	def copyFileTask(name, oldFolderName, newFolderName, queue):
	    '''完成copy一个文件的功能'''
	    fr = open(oldFolderName+'/'+name)
	    fw = open(newFolderName+'/'+name, 'w')

	    content = fr.read()
	    fw.write(content)

	    fr.close()
	    fw.close()

	    queue.put(name)


	def main():
	    time1 = time.time()
	    # 获取要复制的文件夹名称：
	    oldFolderName = input("请输入你要复制的文件夹名称：")

	    # 创建新的文件夹：
	    newFolderName = oldFolderName + '_复件'
	    # print(newFolderName)
	    os.mkdir(newFolderName)

	    # 获取old文件夹中的所有文件名字：
	    filesNames = os.listdir(oldFolderName)
	    # print(filesNames)

	    # 使用多线程的方式拷贝原文件夹中的文件到新的文件夹中。
	    pool = Pool(10)
	    queue = Manager().Queue()

	    for name in filesNames:
	        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue))

	    num = 0
	    allNum = len(filesNames)
	    while True:
	        queue.get()
	        num += 1
	        copyRate = num/allNum
	        print('\rcopy的进度是：%.2f%%' % (copyRate*100), end='')
	        if num == allNum:
	            break
	        print('')
	    time2 = time.time()
	    print('运行时间为：%d s' % (time2 - time1))
	    pool.close()
	if __name__ == "__main__":
	    main()



