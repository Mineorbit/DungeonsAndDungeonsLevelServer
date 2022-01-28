// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0-devel
// 	protoc        v3.14.0
// source: LevelMetaDataList.proto

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

type LevelMetaDataList struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Levels []*LevelMetaData `protobuf:"bytes,1,rep,name=levels,proto3" json:"levels,omitempty"`
}

func (x *LevelMetaDataList) Reset() {
	*x = LevelMetaDataList{}
	if protoimpl.UnsafeEnabled {
		mi := &file_LevelMetaDataList_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LevelMetaDataList) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LevelMetaDataList) ProtoMessage() {}

func (x *LevelMetaDataList) ProtoReflect() protoreflect.Message {
	mi := &file_LevelMetaDataList_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LevelMetaDataList.ProtoReflect.Descriptor instead.
func (*LevelMetaDataList) Descriptor() ([]byte, []int) {
	return file_LevelMetaDataList_proto_rawDescGZIP(), []int{0}
}

func (x *LevelMetaDataList) GetLevels() []*LevelMetaData {
	if x != nil {
		return x.Levels
	}
	return nil
}

var File_LevelMetaDataList_proto protoreflect.FileDescriptor

var file_LevelMetaDataList_proto_rawDesc = []byte{
	0x0a, 0x17, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x4d, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x4c,
	0x69, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x08, 0x4e, 0x65, 0x74, 0x4c, 0x65,
	0x76, 0x65, 0x6c, 0x1a, 0x13, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x4d, 0x65, 0x74, 0x61, 0x44, 0x61,
	0x74, 0x61, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x44, 0x0a, 0x11, 0x4c, 0x65, 0x76, 0x65,
	0x6c, 0x4d, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x4c, 0x69, 0x73, 0x74, 0x12, 0x2f, 0x0a,
	0x06, 0x6c, 0x65, 0x76, 0x65, 0x6c, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x17, 0x2e,
	0x4e, 0x65, 0x74, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x2e, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x4d, 0x65,
	0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x52, 0x06, 0x6c, 0x65, 0x76, 0x65, 0x6c, 0x73, 0x42, 0x35,
	0x5a, 0x33, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x4d, 0x69, 0x6e,
	0x65, 0x6f, 0x72, 0x62, 0x69, 0x74, 0x2f, 0x44, 0x75, 0x6e, 0x67, 0x65, 0x6f, 0x6e, 0x73, 0x41,
	0x6e, 0x64, 0x44, 0x75, 0x6e, 0x67, 0x65, 0x6f, 0x6e, 0x73, 0x4c, 0x65, 0x76, 0x65, 0x6c, 0x53,
	0x65, 0x72, 0x76, 0x65, 0x72, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_LevelMetaDataList_proto_rawDescOnce sync.Once
	file_LevelMetaDataList_proto_rawDescData = file_LevelMetaDataList_proto_rawDesc
)

func file_LevelMetaDataList_proto_rawDescGZIP() []byte {
	file_LevelMetaDataList_proto_rawDescOnce.Do(func() {
		file_LevelMetaDataList_proto_rawDescData = protoimpl.X.CompressGZIP(file_LevelMetaDataList_proto_rawDescData)
	})
	return file_LevelMetaDataList_proto_rawDescData
}

var file_LevelMetaDataList_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_LevelMetaDataList_proto_goTypes = []interface{}{
	(*LevelMetaDataList)(nil), // 0: NetLevel.LevelMetaDataList
	(*LevelMetaData)(nil),     // 1: NetLevel.LevelMetaData
}
var file_LevelMetaDataList_proto_depIdxs = []int32{
	1, // 0: NetLevel.LevelMetaDataList.levels:type_name -> NetLevel.LevelMetaData
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_LevelMetaDataList_proto_init() }
func file_LevelMetaDataList_proto_init() {
	if File_LevelMetaDataList_proto != nil {
		return
	}
	file_LevelMetaData_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_LevelMetaDataList_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LevelMetaDataList); i {
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
			RawDescriptor: file_LevelMetaDataList_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_LevelMetaDataList_proto_goTypes,
		DependencyIndexes: file_LevelMetaDataList_proto_depIdxs,
		MessageInfos:      file_LevelMetaDataList_proto_msgTypes,
	}.Build()
	File_LevelMetaDataList_proto = out.File
	file_LevelMetaDataList_proto_rawDesc = nil
	file_LevelMetaDataList_proto_goTypes = nil
	file_LevelMetaDataList_proto_depIdxs = nil
}
