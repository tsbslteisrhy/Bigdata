"""
    날짜 : 2020/07/22
    이름 : 유효진
    내용 : 파이썬 Hadoop 실습하기
"""

from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

#Hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

#Local /home/bigdata/naver/naver-20-xx-xx 를 하둡 /naver/ 복사
naver = 'home/bigdata/naver/'
hdfs.get_file_dir_status(naver)
{
    "FileStatus":{
        "accessTime":0,
        "blockSize":0,
        "group":"hdfs",
        "length":0,
        "modificationTime":1371737704208,
        "owner":"root",
        "pathSuffix":"",
        "permission":"755",
        "replication":0,
        "type":"DIRECTORY"
    }
}

#Local /home/bigdata/naver/naver-20-xx-xx 를 삭제

#프로그램 종료
print('프로그램 종료...')