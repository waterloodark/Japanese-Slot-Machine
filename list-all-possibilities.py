Last login: Tue Mar 24 12:11:38 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
lune:2020.03.23 日本電動式遊技機工業協同組合 uu$ who
uu       console  Mar 15 12:47 
uu       ttys000  Mar 24 11:15 
uu       ttys001  Mar 24 11:16 
uu       ttys002  Mar 22 12:50 
uu       ttys003  Mar 23 09:48 
uu       ttys004  Mar 24 12:11 
uu       ttys005  Mar 24 12:21 
lune:2020.03.23 日本電動式遊技機工業協同組合 uu$ !s
ssh -Y uu@ballon.inf.uec.ac.jp
uu@ballon.inf.uec.ac.jp's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 5.3.0-40-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

29 packages can be updated.
0 updates are security updates.

Your Hardware Enablement Stack (HWE) is supported until April 2023.
*** System restart required ***
Last login: Tue Mar 24 12:12:51 2020 from 130.153.146.65
uu@ballon:~$ ps aux | grep Pych
uu        6562  0.0  0.0 389284 30172 pts/2    Sl+  11:21   0:03 /home/uu/PycharmProjects/slotmachines/venv/bin/python /usr/local/pycharm-community-2019.3.4/plugins/python-ce/helpers/pydev/pydevconsole.py --mode=client --port=34397
uu       13956  0.0  0.0  24240  1068 pts/11   R+   12:21   0:00 grep --color=auto Pych
uu@ballon:~$ ps aux | grep PyChar
uu        5740 39.2  1.8 10980796 1187428 pts/2 Sl+ 11:16  25:45 /usr/local/pycharm-community-2019.3.4/jbr/bin/java -classpath /usr/local/pycharm-community-2019.3.4/lib/bootstrap.jar:/usr/local/pycharm-community-2019.3.4/lib/extensions.jar:/usr/local/pycharm-community-2019.3.4/lib/util.jar:/usr/local/pycharm-community-2019.3.4/lib/jdom.jar:/usr/local/pycharm-community-2019.3.4/lib/log4j.jar:/usr/local/pycharm-community-2019.3.4/lib/trove4j.jar:/usr/local/pycharm-community-2019.3.4/lib/jna.jar -Xms128m -Xmx2048m -XX:ReservedCodeCacheSize=240m -XX:+UseConcMarkSweepGC -XX:SoftRefLRUPolicyMSPerMB=50 -ea -XX:CICompilerCount=2 -Dsun.io.useCanonPrefixCache=false -Djava.net.preferIPv4Stack=true -Djdk.http.auth.tunneling.disabledSchemes="" -XX:+HeapDumpOnOutOfMemoryError -XX:-OmitStackTraceInFastThrow -Djdk.attach.allowAttachSelf=true -Dkotlinx.coroutines.debug=off -Djdk.module.illegalAccess.silent=true -Dawt.useSystemAAFontSettings=lcd -Dsun.java2d.renderer=sun.java2d.marlin.MarlinRenderingEngine -Dsun.tools.attach.tmp.only=true -XX:ErrorFile=/home/uu/java_error_in_PYCHARM_%p.log -XX:HeapDumpPath=/home/uu/java_error_in_PYCHARM.hprof -Didea.paths.selector=PyCharmCE2019.3 -Djb.vmOptionsFile=/home/uu/.PyCharmCE2019.3/config/pycharm64.vmoptions -Didea.platform.prefix=PyCharmCore com.intellij.idea.Main
uu       13993  0.0  0.0  24240  1012 pts/11   R+   12:21   0:00 grep --color=auto PyChar
uu@ballon:~$ cd PycharmProjects/
uu@ballon:~/PycharmProjects$ cd slotmachines/
uu@ballon:~/PycharmProjects/slotmachines$ ls -alFt
total 1356416
drwxrwxr-x 5 uu uu       4096  3月 24 12:14 ./
-rw-rw-r-- 1 uu uu       7838  3月 24 12:14 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       4096  3月 24 12:13 1600-1.txt
-rw-rw-r-- 1 uu uu       4096  3月 24 12:12 1600-3.txt
-rw-rw-r-- 1 uu uu       4096  3月 24 12:11 1600-2.txt
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea/
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints/
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv/
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ../
uu@ballon:~/PycharmProjects/slotmachines$ cat 1600-1.txt
Script started on 2020-03-24 12:07:37+0900
uu@ballon:~/PycharmProjects/slotmachines$ python listing-patterns-v5.py 1
[0.675813698630137, 0.1822, 0.136986301369863, 0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0.675813698630137, 0.1822, 0.136986301369863, 0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0.675813698630137, 0.1822, 0.136986301369863, 0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[0.675813698630137, 0.1822, 0.136986301369863, 0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[24, [24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24]]
[3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 8, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 411997), 0, 0]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 414412), 10, 385]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 432152), 20, 2170]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 489842), 30, 6490]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 633226), 40, 14510]
[datetime.datetime(2020, 3, 24, 12, 7, 45, 922561), 50, 27338]
[datetime.datetime(2020, 3, 24, 12, 7, 46, 438795), 60, 46163]
[datetime.datetime(2020, 3, 24, 12, 7, 47, 291908), 70, 72072]
[datetime.datetime(2020, 3, 24, 12, 7, 48, 608997), 80, 106272]
[datetime.datetime(2020, 3, 24, 12, 7, 50, 513449), 90, 149835]
[datetime.datetime(2020, 3, 24, 12, 7, 53, 207456), 100, 203980]
[datetime.datetime(2020, 3, 24, 12, 7, 56, 852940), 110, 269602]
[datetime.datetime(2020, 3, 24, 12, 8, 1, 647119), 120, 347002]
[datetime.datetime(2020, 3, 24, 12, 8, 7, 916513), 130, 436169]
[datetime.datetime(2020, 3, 24, 12, 8, 15, 727835), 140, 537109]
[datetime.datetime(2020, 3, 24, 12, 8, 25, 361344), 150, 649822]
[datetime.datetime(2020, 3, 24, 12, 8, 37, 431160), 160, 774302]
[datetime.datetime(2020, 3, 24, 12, 8, 51, 528896), 170, 910561]
[datetime.datetime(2020, 3, 24, 12, 9, 8, 43441), 180, 1058581]
[datetime.datetime(2020, 3, 24, 12, 9, 27, 319277), 190, 1218386]
[datetime.datetime(2020, 3, 24, 12, 9, 49, 516503), 200, 1389946]
[datetime.datetime(2020, 3, 24, 12, 10, 15, 430023), 210, 1573297]
[datetime.datetime(2020, 3, 24, 12, 10, 44, 576288), 220, 1768397]
[datetime.datetime(2020, 3, 24, 12, 11, 17, 961783), 230, 1975294]
[datetime.datetime(2020, 3, 24, 12, 11, 55, 19695), 240, 2193934]
[datetime.datetime(2020, 3, 24, 12, 12, 37, 56585), 250, 2424374]
[datetime.datetime(2020, 3, 24, 12, 13, uu@ballon:~/PycharmProjects/slotmachines$ 
uu@ballon:~/PycharmProjects/slotmachines$ pwd
/home/uu/PycharmProjects/slotmachines
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356432
drwxrwxr-x 5 uu uu       4096  3月 24 12:23 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-3.txt
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ echo "# Japanese-Slot-Machine" >> README.md
uu@ballon:~/PycharmProjects/slotmachines$ git init
Initialized empty Git repository in /home/uu/PycharmProjects/slotmachines/.git/
uu@ballon:~/PycharmProjects/slotmachines$ git add README.md
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "first commit"
[master (root-commit) 1d9bfa6] first commit
 Committer: uu <uu@ballon.inf.uec.ac.jp>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 README.md
uu@ballon:~/PycharmProjects/slotmachines$ git remote add origin https://github.com/waterloodark/Japanese-Slot-Machine.git
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': ^C
uu@ballon:~/PycharmProjects/slotmachines$     git config --global --edit
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "first commit"
On branch master
Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

nothing added to commit but untracked files present
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356440
drwxrwxr-x 6 uu uu       4096  3月 24 12:29 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 8 uu uu       4096  3月 24 12:31 .git
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-3.txt
-rw-rw-r-- 1 uu uu         24  3月 24 12:29 README.md
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ cp listing-patterns-v0.py listing-patterns.py
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "first commit" listing-patterns.py 
error: pathspec 'listing-patterns.py' did not match any file(s) known to git.
uu@ballon:~/PycharmProjects/slotmachines$ git remote add origin https://github.com/waterloodark/Japanese-Slot-Machine.git
fatal: remote origin already exists.
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Counting objects: 3, done.
Writing objects: 100% (3/3), 231 bytes | 231.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/waterloodark/Japanese-Slot-Machine.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356444
drwxrwxr-x 6 uu uu       4096  3月 24 12:31 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 8 uu uu       4096  3月 24 12:32 .git
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-3.txt
-rw-rw-r-- 1 uu uu         24  3月 24 12:29 README.md
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       1289  3月 24 12:31 listing-patterns.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ git add listing-patterns.py 
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/waterloodark/Japanese-Slot-Machine.git/'
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 0. 2020.03.22.0219p" 
[master 7b6abad] pattern listing script version 0. 2020.03.22.0219p
 Committer: uu <uu@ballon.inf.uec.ac.jp>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 40 insertions(+)
 create mode 100644 listing-patterns.py
uu@ballon:~/PycharmProjects/slotmachines$ git config --global user.name "waterloo" git config --global user.email waterloo.dark@gmail.com
usage: git config [<options>]

Config file location
    --global              use global config file
    --system              use system config file
    --local               use repository config file
    -f, --file <file>     use given config file
    --blob <blob-id>      read config from given blob object

Action
    --get                 get value: name [value-regex]
    --get-all             get all values: key [value-regex]
    --get-regexp          get values for regexp: name-regex [value-regex]
    --get-urlmatch        get value specific for the URL: section[.var] URL
    --replace-all         replace all matching variables: name value [value_regex]
    --add                 add a new variable: name value
    --unset               remove a variable: name [value-regex]
    --unset-all           remove all matches: name [value-regex]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    -e, --edit            open an editor
    --get-color           find the color configured: slot [default]
    --get-colorbool       find the color setting: slot [stdout-is-tty]

Type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --null            terminate values with NUL byte
    --name-only           show variable names only
    --includes            respect include directives on lookup
    --show-origin         show origin of config (file, standard input, blob, command line)

uu@ballon:~/PycharmProjects/slotmachines$ git config --global user.name "waterloo"
uu@ballon:~/PycharmProjects/slotmachines$ git config --global user.email waterloo.dark@gmail.com
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 0. 2020.03.22.0219p" 
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

nothing added to commit but untracked files present
uu@ballon:~/PycharmProjects/slotmachines$ git add listing-patterns.py 
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 0. 2020.03.22.0219p" 
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

nothing added to commit but untracked files present
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Counting objects: 3, done.
Delta compression using up to 16 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 688 bytes | 688.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/waterloodark/Japanese-Slot-Machine.git
   1d9bfa6..7b6abad  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356448
drwxrwxr-x 6 uu uu       4096  3月 24 12:31 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 8 uu uu       4096  3月 24 12:37 .git
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu      12288  3月 24 12:34 1600-3.txt
-rw-rw-r-- 1 uu uu         24  3月 24 12:29 README.md
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       1289  3月 24 12:31 listing-patterns.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ cp listing-patterns-v1.py listing-patterns.py 
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 2. 2020.03.22 0432p" 
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	modified:   listing-patterns.py

Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

no changes added to commit
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 2. 2020.03.22 0432p" 
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	modified:   listing-patterns.py

Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

no changes added to commit
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356452
drwxrwxr-x 6 uu uu       4096  3月 24 12:31 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 8 uu uu       4096  3月 24 12:38 .git
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu      12288  3月 24 12:34 1600-3.txt
-rw-rw-r-- 1 uu uu         24  3月 24 12:29 README.md
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       4246  3月 24 12:37 listing-patterns.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ git commit -m "pattern listing script version 2. 2020.03.22 0432p" 
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	modified:   listing-patterns.py

Untracked files:
	.idea/
	.ipynb_checkpoints/
	1600-1.txt
	1600-2.txt
	1600-3.txt
	Untitled.ipynb
	aa.py
	aa.py~
	listing-patterns-v0.py
	listing-patterns-v1.py
	listing-patterns-v2-model-1.py
	listing-patterns-v2-model-1.py.log.txt
	listing-patterns-v2-model-1.py~
	listing-patterns-v2-model-2.py
	listing-patterns-v2-model-2.py.log.txt
	listing-patterns-v2-model-2.py~
	listing-patterns-v2-model-3.py
	listing-patterns-v2-model-3.py.log.txt
	listing-patterns-v2-model-3.py~
	listing-patterns-v2.py~
	listing-patterns-v4-model-2.py
	listing-patterns-v4-model-2.py~
	listing-patterns-v4-model-3.py
	listing-patterns-v4-model-3.py~
	listing-patterns-v4.py
	listing-patterns-v4.py.log.txt
	listing-patterns-v4.py~
	listing-patterns-v5.py
	models-v1.py
	models-v1.py~
	states-1600-1.csv
	states-1600-2.csv
	states-1600-3.csv
	states-aa-1.csv
	test-history.csv
	test-states.csv
	texput.log
	venv/

no changes added to commit
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ emas -nw listing-patterns.py 

Command 'emas' not found, did you mean:

  command 'emacs' from snap emacs (26.3)
  command 'emar' from deb emscripten
  command 'emacs' from deb emacs25
  command 'emacs' from deb emacs25-nox
  command 'emacs' from deb e3
  command 'emacs' from deb emacs25-lucid
  command 'emacs' from deb jove

See 'snap info <snapname>' for additional versions.

uu@ballon:~/PycharmProjects/slotmachines$ emacs -nw listing-patterns.py 
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin master
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ git push -u origin masterg^C
uu@ballon:~/PycharmProjects/slotmachines$ git push 
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ git push origin
Username for 'https://github.com': waterlodark
Password for 'https://waterlodark@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/waterloodark/Japanese-Slot-Machine.git/'
uu@ballon:~/PycharmProjects/slotmachines$ git push origin
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ git pull
Already up to date.
uu@ballon:~/PycharmProjects/slotmachines$ ls -al
total 1356452
drwxrwxr-x 6 uu uu       4096  3月 24 12:31 .
drwxrwxr-x 3 uu uu       4096  3月 22 12:23 ..
drwxrwxr-x 8 uu uu       4096  3月 24 12:40 .git
drwxrwxr-x 3 uu uu       4096  3月 24 11:58 .idea
drwxrwxr-x 2 uu uu       4096  3月 22 21:32 .ipynb_checkpoints
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-1.txt
-rw-rw-r-- 1 uu uu       8192  3月 24 12:24 1600-2.txt
-rw-rw-r-- 1 uu uu      12288  3月 24 12:34 1600-3.txt
-rw-rw-r-- 1 uu uu         24  3月 24 12:29 README.md
-rw-rw-r-- 1 uu uu       8629  3月 22 22:12 Untitled.ipynb
-rw-rw-r-- 1 uu uu       2739  3月 23 03:24 aa.py
-rw-rw-r-- 1 uu uu       2738  3月 23 03:21 aa.py~
-rw-rw-r-- 1 uu uu       1289  3月 22 14:19 listing-patterns-v0.py
-rw-rw-r-- 1 uu uu       4246  3月 22 16:42 listing-patterns-v1.py
-rw-rw-r-- 1 uu uu       2740  3月 23 01:35 listing-patterns-v2-model-1.py
-rw-rw-r-- 1 uu uu      12965  3月 23 05:53 listing-patterns-v2-model-1.py.log.txt
-rw-rw-r-- 1 uu uu       2734  3月 23 01:15 listing-patterns-v2-model-1.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:34 listing-patterns-v2-model-2.py
-rw-rw-r-- 1 uu uu       2938  3月 23 20:46 listing-patterns-v2-model-2.py.log.txt
-rw-rw-r-- 1 uu uu       3726  3月 23 01:29 listing-patterns-v2-model-2.py~
-rw-rw-r-- 1 uu uu       3782  3月 23 01:42 listing-patterns-v2-model-3.py
-rw-rw-r-- 1 uu uu        630  3月 23 20:47 listing-patterns-v2-model-3.py.log.txt
-rw-rw-r-- 1 uu uu       3782  3月 23 01:41 listing-patterns-v2-model-3.py~
-rw-rw-r-- 1 uu uu       5159  3月 22 23:18 listing-patterns-v2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-2.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:09 listing-patterns-v4-model-2.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:30 listing-patterns-v4-model-3.py
-rw-rw-r-- 1 uu uu       5683  3月 23 21:10 listing-patterns-v4-model-3.py~
-rw-rw-r-- 1 uu uu       5650  3月 23 21:29 listing-patterns-v4.py
-rw-rw-r-- 1 uu uu      14288  3月 24 12:07 listing-patterns-v4.py.log.txt
-rw-rw-r-- 1 uu uu       5683  3月 23 20:41 listing-patterns-v4.py~
-rw-rw-r-- 1 uu uu       8541  3月 24 12:23 listing-patterns-v5.py
-rw-rw-r-- 1 uu uu       4246  3月 24 12:37 listing-patterns.py
-rw-rw-r-- 1 uu uu       6966  3月 22 22:51 models-v1.py
-rw-rw-r-- 1 uu uu          0  3月 22 21:34 models-v1.py~
-rw-rw-r-- 1 uu uu   40538511  3月 23 21:53 states-1600-1.csv
-rw-rw-r-- 1 uu uu  268838526  3月 24 00:48 states-1600-2.csv
-rw-rw-r-- 1 uu uu 1034265192  3月 24 12:03 states-1600-3.csv
-rw-rw-r-- 1 uu uu     735131  3月 23 03:24 states-aa-1.csv
-rw-rw-r-- 1 uu uu          5  3月 24 11:57 test-history.csv
-rw-rw-r-- 1 uu uu   44359334  3月 24 11:57 test-states.csv
-rw-rw-r-- 1 uu uu        813  3月 23 03:29 texput.log
drwxrwxr-x 5 uu uu       4096  3月 22 12:23 venv
uu@ballon:~/PycharmProjects/slotmachines$ git pull
Already up to date.
uu@ballon:~/PycharmProjects/slotmachines$ emac s-nw listing-patterns.py 

Command 'emac' not found, did you mean:

  command 'emcc' from deb emscripten
  command 'gmac' from deb tkgate
  command 'emacs' from deb emacs25
  command 'emacs' from deb emacs25-nox
  command 'emacs' from deb e3
  command 'emacs' from deb emacs25-lucid
  command 'emacs' from deb jove
  command 'jmac' from deb libjmac-java
  command 'emar' from deb emscripten

Try: sudo apt install <deb name>

uu@ballon:~/PycharmProjects/slotmachines$ emacs -nw listing-patterns.py 
uu@ballon:~/PycharmProjects/slotmachines$ git push
Username for 'https://github.com': waterloodark
Password for 'https://waterloodark@github.com': 
Everything up-to-date
uu@ballon:~/PycharmProjects/slotmachines$ emacs -nw listing-patterns.py ^C
uu@ballon:~/PycharmProjects/slotmachines$ emacs -nw listing-patterns-v0.py 
uu@ballon:~/PycharmProjects/slotmachines$ more c^C
uu@ballon:~/PycharmProjects/slotmachines$ emacs -nw listing-patterns-v1.py 

File Edit Options Buffers Tools Python Help                                                                                             
p_free = 1/7.3
p_hand = 0.1634
p_rb = 1/315
p_bb = 1/259
p_blank = 1 - p_free - p_hand - p_rb - p_bb
payout_hand = 8
payout_rb = 8
payout_bb = 15
slotin_free = 0
slotin_lottary = 3
slotin_bonus_regular = 3
slotin_bonus_big = 3
state_lottary = [0, 2, 11, 26]
state_free = [1]
P = [[p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [p_blank, p_free, p_hand, p_rb, 0, 0, 0, 0, 0, 0, 0, p_bb, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(len(P))
#for i in range(len(P)):                                                                                                                
#    print(len(P[i]))                                                                                                                   
s = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
states = {(0, 0): 1}

                   import datetime as dt


timestamp_1 = dt.datetime.now()
for i in range(6000):
    states_new = {}
    for state in list(states.keys()):
        p_vec = P[state[0]]
        for i in range(len(p_vec)):
            if p_vec[i] > 0:
                if i is 1:
                    slot_in = 0
                else:
                    slot_in = 3
                if i is 2:
                    pay_out = payout_hand
                elif i in range(3,10):
                    pay_out = payout_rb
                    state_next = (i + 1, state[1] - slot_in + pay_out)
                elif i is 10:
                    pay_out = payout_rb
                    state_next = (0, state[1] - slot_in + pay_out)
                elif i in range(11,25):
                    pay_out = payout_bb
                    state_next = (i + 1, state[1] - slot_in + pay_out)
                elif i is 25:
                    pay_out = payout_bb
                    state_next = (0, state[1] - slot_in + pay_out)
                else:
                    pay_out = 0
                    state_next = (0, state[1] - slot_in + pay_out)
                if state_next in states_new.keys():
                    states_new[state_next] += states[state] * p_vec[i]
                else:
                    states_new[state_next] = states[state] * p_vec[i]
    states = states_new
timestamp_2 = dt.datetime.now()
# print(states)                                                                                                                         
print(timestamp_1)
print(timestamp_2)
print(timestamp_2 - timestamp_1)
print(len(states))
