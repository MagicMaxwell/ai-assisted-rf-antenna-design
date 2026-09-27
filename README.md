# 人工智能辅助的射频电路及天线设计仿真

AI-Assisted Design and Simulation of RF Circuits and Antennas

面向硕士及博士研究生的课程资料。课程为48学时、3学分，秋学期开设，采用大作业考核。通过COMSOL、CST、HFSS、ADS的案例学习，掌握AI辅助建模、设计、仿真、数据核验与结果研讨的基本方法。

## 实验上机手册

点击下表进入Word文件页面，使用 **Download raw file** 下载。也可通过仓库 **Code → Download ZIP** 获取全部自编资料。

| 实验 | Word手册 | 主软件 | 建议上机学时 |
| --- | --- | --- | ---: |
| 超材料 | [周期谐振单元与AI辅助设计](manuals/01_metamaterials_lab.docx) | CST、HFSS、COMSOL | 6 |
| 天线 | [2.45 GHz贴片天线与跨软件验证](manuals/02_antennas_lab.docx) | HFSS、CST、COMSOL | 6 |
| 射频无源及有源电路 | [匹配、功分器、滤波器、小信号与非线性压缩](manuals/03_rf_passive_active_lab.docx) | ADS | 8 |
| 多物理场 | [射频电磁热耦合与能量核验](manuals/04_multiphysics_lab.docx) | COMSOL、CST | 4 |

每份手册包含参数与几何、顺序操作、核验指标、AI任务、结果记录、问题排查和提交评价。24学时是这组实验的建议上机安排，供48学时课程统筹；拓展任务按基础与研究方向选做。

## 官方手册及案例

查看 [21份官方资料索引](references/official-resources.md)，覆盖入门、高频、周期/Floquet、天线、平面EM、匹配、放大器、谐波平衡、滤波器及电磁热案例。官方PDF采用官网入口，不在本仓库整本转载。

## 配套文件

- [辅助文件说明](examples/00_辅助文件使用说明.md)
- [小信号教学二端口S2P](examples/educational_active_2port.s2p)
- [非线性限幅放大器Verilog-A](examples/edu_soft_limiter.va)
- [理论尺寸与模型核验Python](examples/reference_calculations.py)
- [实验数据字段与AI记录模板](examples/实验数据字段与AI记录模板.md)

Python脚本仅使用标准库。进入examples目录执行 `python reference_calculations.py` 可重算理论起点和教学模型的一致性；其输出不代表电磁求解或ADS实际运行结果。

## 学习与提交

先完成固定参数基准模型，再做AI辅助扫描、分析与改进，最后回到原求解器独立核验。保存工程、参数、原始数据、AI提示及修正记录，提交实验报告和可复现的大作业。不得以AI预测或生成数值替代实际仿真结果。

当前已完成资料完整性、理论计算和Word排版核验，完整求解工程仍需教师在教学机试运行；菜单、模块许可、计算时长与拟定阈值以试运行结果为准。S2P和限幅模型为课程自编示例，不是商业器件实测数据；Verilog-A需在本机ADS导入并验证。

## 资料使用

本仓库用于课程教学和学习。第三方官方资料的版权归原权利人所有，请按官方入口访问并遵守相应条款。课程自编资料未另行指定开放授权协议。
