# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Data: 属性数据
        :type Data: str
        :param Method: 请求类型
        :type Method: str
        :param DeviceId: 设备ID，该字段有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Data = None
        self.Method = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")
        self.Method = params.get("Method")
        self.DeviceId = params.get("DeviceId")


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回信息
        :type Data: str
        :param Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备参数描述。
        :type Data: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        """
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    """CreateStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称
        :type ProductName: str
        :param CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param ProductType: 产品类型
        :type ProductType: int
        :param EncryptionType: 加密类型
        :type EncryptionType: str
        :param NetType: 连接类型
        :type NetType: str
        :param DataProtocol: 数据协议
        :type DataProtocol: int
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param ProjectId: 产品的项目ID
        :type ProjectId: str
        """
        self.ProductName = None
        self.CategoryId = None
        self.ProductType = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.ProductType = params.get("ProductType")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.ProjectId = params.get("ProjectId")


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 区间开始时间
        :type MinTime: int
        :param MaxTime: 区间结束时间
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FieldName: 属性字段名称
        :type FieldName: str
        :param Limit: 返回条数
        :type Limit: int
        :param Context: 检索上下文
        :type Context: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param FieldName: 属性字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息
        :type Device: :class:`tencentcloud.iotexplorer.v20190423.models.DeviceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = DeviceInfo()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        """
        :param Project: 返回信息
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntryEx()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品详情
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeviceData(AbstractModel):
    """DeviceData

    """

    def __init__(self):
        """
        :param DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param DeviceName: 设备名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePrivateKey: str
        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevicePsk: str
        """
        self.DeviceCert = None
        self.DeviceName = None
        self.DevicePrivateKey = None
        self.DevicePsk = None


    def _deserialize(self, params):
        self.DeviceCert = params.get("DeviceCert")
        self.DeviceName = params.get("DeviceName")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.DevicePsk = params.get("DevicePsk")


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        """
        :param Time: 时间点，毫秒时间戳
        :type Time: str
        :param Value: 字段取值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Status: 0: 离线, 1: 在线, 2: 获取失败, 3 未激活
        :type Status: int
        :param DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LoginTime: 最后一次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param Version: 设备固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param DeviceCert: 设备证书
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        """
        self.DeviceName = None
        self.Status = None
        self.DevicePsk = None
        self.FirstOnlineTime = None
        self.LoginTime = None
        self.CreateTime = None
        self.Version = None
        self.DeviceCert = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.DevicePsk = params.get("DevicePsk")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LoginTime = params.get("LoginTime")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self.TimeStamp = None
        self.ProductId = None
        self.DeviceName = None
        self.EventId = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EventId = params.get("EventId")
        self.Type = params.get("Type")
        self.Data = params.get("Data")


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-100
        :type Limit: int
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetDeviceListResponse(AbstractModel):
    """GetDeviceList返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 返回的设备列表, 注意列表设备的 DevicePsk 为空, 要获取设备的 DevicePsk 请使用 DescribeDevice
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceInfo
        :param Total: 产品下的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetProjectListRequest(AbstractModel):
    """GetProjectList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 个数限制
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回参数结构体

    """

    def __init__(self):
        """
        :param Projects: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Projects: list of ProjectEntryEx
        :param Total: 列表项个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    """GetStudioProductList请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DevStatus: 产品DevStatus
        :type DevStatus: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.ProjectId = None
        self.DevStatus = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DevStatus = params.get("DevStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回参数结构体

    """

    def __init__(self):
        """
        :param Products: 产品列表
        :type Products: list of ProductEntry
        :param Total: 产品数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class ListEventHistoryRequest(AbstractModel):
    """ListEventHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Type: 搜索的事件类型
        :type Type: str
        :param StartTime: 起始时间, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param EndTime: 结束时间, 为0 表示当前时间
        :type EndTime: int
        :param Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param Size: 单次获取的历史数据项目的最大数量
        :type Size: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")


class ListEventHistoryResponse(AbstractModel):
    """ListEventHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Total = None
        self.Listover = None
        self.EventHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Total = params.get("Total")
        self.Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self.EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self.EventHistory.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        """
        :param Project: 项目详情
        :type Project: :class:`tencentcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param ModuleId: 模型ID
        :type ModuleId: int
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDesc = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDesc = params.get("ProductDesc")
        self.ModuleId = params.get("ModuleId")


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品描述
        :type Product: :class:`tencentcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class ProductEntry(AbstractModel):
    """产品详情

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param CategoryId: 产品分组模板ID
        :type CategoryId: int
        :param EncryptionType: 加密类型
        :type EncryptionType: str
        :param NetType: 连接类型
        :type NetType: str
        :param DataProtocol: 数据协议
        :type DataProtocol: int
        :param ProductDesc: 产品描述
        :type ProductDesc: str
        :param DevStatus: 状态
        :type DevStatus: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param UpdateTime: 更新时间
        :type UpdateTime: int
        :param Region: 区域
        :type Region: str
        :param ProductType: 产品类型
        :type ProductType: int
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ModuleId: 产品ModuleId
        :type ModuleId: int
        """
        self.ProductId = None
        self.ProductName = None
        self.CategoryId = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.DevStatus = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Region = None
        self.ProductType = None
        self.ProjectId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.DevStatus = params.get("DevStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleId = params.get("ModuleId")


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelDefine: 模型定义
        :type ModelDefine: str
        :param UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None
        self.CategoryModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.CategoryModel = params.get("CategoryModel")


class ProjectEntry(AbstractModel):
    """项目详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param CreateTime: 创建时间，unix时间戳
        :type CreateTime: int
        :param UpdateTime: 更新时间，unix时间戳
        :type UpdateTime: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProjectEntryEx(AbstractModel):
    """项目详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDesc: 项目描述
        :type ProjectDesc: str
        :param CreateTime: 项目创建时间，unix时间戳
        :type CreateTime: int
        :param UpdateTime: 项目更新时间，unix时间戳
        :type UpdateTime: int
        :param ProductCount: 产品数量
        :type ProductCount: int
        :param NativeAppCount: NativeApp数量
        :type NativeAppCount: int
        :param WebAppCount: WebApp数量
        :type WebAppCount: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ProductCount = None
        self.NativeAppCount = None
        self.WebAppCount = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ProductCount = params.get("ProductCount")
        self.NativeAppCount = params.get("NativeAppCount")
        self.WebAppCount = params.get("WebAppCount")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DevStatus: 产品DevStatus
        :type DevStatus: str
        """
        self.ProductId = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevStatus = params.get("DevStatus")


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param Limit: 列表Limit
        :type Limit: int
        :param Offset: 列表Offset
        :type Offset: int
        :param DevStatus: 产品Status
        :type DevStatus: str
        """
        self.ProjectId = None
        self.ProductName = None
        self.Limit = None
        self.Offset = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductName = params.get("ProductName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DevStatus = params.get("DevStatus")


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Products: 产品列表
        :type Products: list of ProductEntry
        :param Total: 产品数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")