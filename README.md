# flask_pig_admin_be
种猪信息测定管理系统

## 导出数据库数据的shell
```shell
/Applications/MAMP/Library/bin/mysql  -u root --password=root --database=pig --execute='SELECT `id`, `earid`, `stationid`, `foodintake`, `weight`, `bodylong`, `bodywidth`, `bodyheight`, `bodytemperature`, `systime` FROM `pig_info` LIMIT 0, 10000000 '  | sed 's/  /,/g;s/\n//g' > pig.csv

# sed 的用法
# sed 's/ /,/g;    s/^/"/;   s/$/"/;   s/\n//g'

# s/ /,/g; 将 tab 字符转换成 ，
# s/^/"/; 在一行的开始加 "
# s/$/"/; 在一行的末尾加 "
# s/\n//g  在行位加上 \n 换行

```

