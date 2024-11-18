# DDL_MANAGER
基于MYSQL建立的ddl管理器。支持自然语言建立ddl条目。

## 部署
- 在info_generator.py中填写相关信息并运行程序

## 功能

- 管理ddl

## 使用方法

### SHOW

使用`SHOW`命令来查询DDL1表中的数据。你需要指定一个排序的字段和一个排序的方向。

#### 语法

```
SHOW [字段] [排序方向]
```

#### 参数

- **字段**：可以是`DEADLINE`、`IMPORTANCE`、`DIFFICULTY`、`TIME`或`GROUP`。
- **排序方向**：可以是`ASC`（升序）或`DESC`（降序）。

#### 示例

- 显示DDL1表中按截止日期升序排列的数据：
  ```
  SHOW DEADLINE ASC
  ```

- 显示DDL1表中按重要性降序排列的数据：
  ```
  SHOW IMPORTANCE DESC
  ```

- 显示DDL1表中按估计时间分组，并按总时间降序排列的数据：
  ```
  SHOW GROUP DESC
  ```

### HELP

如果你不确定如何使用任何命令，可以使用`HELP`命令获取帮助。



## 注意事项

- 确保你的MySQL数据库连接信息是正确的，包括主机名、数据库名、用户名和密码。
- 确保DDL1表存在于你的数据库中，并且包含正确的字段。

## 联系

如果你有任何问题或需要进一步的帮助，请随时联系我们。
这个README文件提供了一个基本的介绍和使用指南，用户可以根据这个指南来使用`show`命令。


