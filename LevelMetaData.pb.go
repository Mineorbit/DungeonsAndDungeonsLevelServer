// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.19.0
// source: LevelMetaData.proto

package main

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type LevelMetaData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	LocalLevelId  int32  `protobuf:"varint,1,opt,name=localLevelId,proto3" json:"localLevelId,omitempty"`
	UniqueLevelId int64  `protobuf:"varint,2,opt,name=uniqueLevelId,proto3" json:"uniqueLevelId,omitempty"`
	FullName      string `protobuf:"bytes,3,opt,name=FullName,proto3" json:"FullName,omitempty"`
	Description   string `protobuf:"bytes,4,opt,name=Description,proto3" json:"Description,omitempty"`
	AvailBlue     bool   `protobuf:"varint,5,opt,name=availBlue,proto3" json:"availBlue,omitempty"`
	AvailYellow   bool   `protobuf:"varint,6,opt,name=availYellow,proto3" json:"availYellow,omitempty"`
	AvailRed      bool   `protobuf:"varint,7,opt,name=availRed,proto3" json:"availRed,omitempty"`
	AvailGreen    bool   `protobuf:"varint,8,opt,name=availGreen,proto3" json:"availGreen,omitempty"`
}

func (x *LevelMetaData) Reset() {
	*x = LevelMetaData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_LevelMetaData_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LevelMetaData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LevelMetaData) ProtoMessage() {}

func (x *LevelMetaData) ProtoReflect() protoreflect.Message {
	mi := &file_LevelMetaData_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LevelMetaData.ProtoReflect.Descriptor instead.
func (*LevelMetaData) Descriptor() ([]byte, []int) {
	return file_LevelMetaData_proto_rawDescGZIP(), []int{0}
}

func (x *LevelMetaData) GetLocalLevelId() int32 {
	if x != nil {
		return x.LocalLevelId
	}
	return 0
}

func (x *LevelMetaData) GetUniqueLevelId() int64 {
	if x != nil {
		return x.UniqueLevelId
	}
	return 0
}

func (x *LevelMetaData) GetFullName() string {
	if x != nil {
		return x.FullName
	}
	return ""
}

func (x *LevelMetaData) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *LevelMetaData) GetAvailBlue() bool {
	if x != nil {
		return x.AvailBlue
	}
	return false
}

func (x *LevelMetaData) GetAvailYellow() bool {
	if x != nil {
		return x.AvailYellow
	}
	return false
}

func (x *LevelMetaData) GetAvailRed() bool {
	if x != nil {
		return x.AvailRed
	}
	return false
}

func (x *LevelMetaData) GetAvailGreen() bool {
	if x != nil {
		return x.AvailGreen
	}
	return false
}

var File_LevelMetaData_proto protoreflect.FileDescriptor

var file_LevelMetaData_proto_rawDesc = []byte{
	0x0a, 0x13, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x4d, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x08, 0x4e, 0x65, 0x74, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x22,
	0x93, 0x02, 0x0a, 0x0d, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x4d, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74,
	0x61, 0x12, 0x22, 0x0a, 0x0c, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x49,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0c, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x4c, 0x65,
	0x76, 0x65, 0x6c, 0x49, 0x64, 0x12, 0x24, 0x0a, 0x0d, 0x75, 0x6e, 0x69, 0x71, 0x75, 0x65, 0x4c,
	0x65, 0x76, 0x65, 0x6c, 0x49, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0d, 0x75, 0x6e,
	0x69, 0x71, 0x75, 0x65, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x49, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x46,
	0x75, 0x6c, 0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x46,
	0x75, 0x6c, 0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x44, 0x65, 0x73, 0x63, 0x72,
	0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x44, 0x65,
	0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1c, 0x0a, 0x09, 0x61, 0x76, 0x61,
	0x69, 0x6c, 0x42, 0x6c, 0x75, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x61, 0x76,
	0x61, 0x69, 0x6c, 0x42, 0x6c, 0x75, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x61, 0x76, 0x61, 0x69, 0x6c,
	0x59, 0x65, 0x6c, 0x6c, 0x6f, 0x77, 0x18, 0x06, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0b, 0x61, 0x76,
	0x61, 0x69, 0x6c, 0x59, 0x65, 0x6c, 0x6c, 0x6f, 0x77, 0x12, 0x1a, 0x0a, 0x08, 0x61, 0x76, 0x61,
	0x69, 0x6c, 0x52, 0x65, 0x64, 0x18, 0x07, 0x20, 0x01, 0x28, 0x08, 0x52, 0x08, 0x61, 0x76, 0x61,
	0x69, 0x6c, 0x52, 0x65, 0x64, 0x12, 0x1e, 0x0a, 0x0a, 0x61, 0x76, 0x61, 0x69, 0x6c, 0x47, 0x72,
	0x65, 0x65, 0x6e, 0x18, 0x08, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0a, 0x61, 0x76, 0x61, 0x69, 0x6c,
	0x47, 0x72, 0x65, 0x65, 0x6e, 0x42, 0x35, 0x5a, 0x33, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e,
	0x63, 0x6f, 0x6d, 0x2f, 0x4d, 0x69, 0x6e, 0x65, 0x6f, 0x72, 0x62, 0x69, 0x74, 0x2f, 0x44, 0x75,
	0x6e, 0x67, 0x65, 0x6f, 0x6e, 0x73, 0x41, 0x6e, 0x64, 0x44, 0x75, 0x6e, 0x67, 0x65, 0x6f, 0x6e,
	0x73, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_LevelMetaData_proto_rawDescOnce sync.Once
	file_LevelMetaData_proto_rawDescData = file_LevelMetaData_proto_rawDesc
)

func file_LevelMetaData_proto_rawDescGZIP() []byte {
	file_LevelMetaData_proto_rawDescOnce.Do(func() {
		file_LevelMetaData_proto_rawDescData = protoimpl.X.CompressGZIP(file_LevelMetaData_proto_rawDescData)
	})
	return file_LevelMetaData_proto_rawDescData
}

var file_LevelMetaData_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_LevelMetaData_proto_goTypes = []interface{}{
	(*LevelMetaData)(nil), // 0: NetLevel.LevelMetaData
}
var file_LevelMetaData_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_LevelMetaData_proto_init() }
func file_LevelMetaData_proto_init() {
	if File_LevelMetaData_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_LevelMetaData_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LevelMetaData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_LevelMetaData_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_LevelMetaData_proto_goTypes,
		DependencyIndexes: file_LevelMetaData_proto_depIdxs,
		MessageInfos:      file_LevelMetaData_proto_msgTypes,
	}.Build()
	File_LevelMetaData_proto = out.File
	file_LevelMetaData_proto_rawDesc = nil
	file_LevelMetaData_proto_goTypes = nil
	file_LevelMetaData_proto_depIdxs = nil
}
