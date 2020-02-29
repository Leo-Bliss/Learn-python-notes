<p>@Time        :    2020/2/29 0029 14:44</p>
<p>@Author      :    tb_youth</p>
<p>@FileName    :    sqlite基础知识.md</p>
<p>@Description :    workLog</p>
<p>@Blog        :    https://blog.csdn.net/tb_youth</p>

# sqlite基础知识

------

<p>@Daily English</p>

> ...

> ...

## 表格信息查询
1. 查询某个数据库中所有的表（详细信息）：

```sql
select * from sqlite_master where type="table";
```
2. 查看某张表的详细信息：
```sql
select * from sqlite_master where type="table" and name="table_name";
```
3. 查看某张表的数据结构(字段类型)：
```sql
pragma table_info("table_name");
```
## sqlite3 数据类型

1. INTEGER:整型根据数值大小按不同的字节(1,2,4,6,8)存储
2. REAL:浮点型，以8字节IEEE浮点数存储
3. TEXT:文本字符串，使用数据库编码（UTF-8,UTF-16BE,UTF-16LE）存储
4. BOLB:数据块，按输入格式（原样）存储
5. NULL:以NULL存储
