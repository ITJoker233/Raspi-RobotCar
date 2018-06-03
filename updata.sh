#!/usr/bin/env sh
basepath=$(cd `dirname $0`; pwd)
echo "\033[32mcurrent dir is: $basepath\033[0m"
cd $basepath"/Car/"
subs=$(cat .gitmodules | grep "path =" | cut -d= -f 2)
for rop in $subs
do
        echo "\033[32mnow in: $rop\033[0m"
        cd $rop
        git fetch --all  
        git reset --hard origin/master 
        git checkout master
        git pull
        cd $basepath"/Car/"
done 
