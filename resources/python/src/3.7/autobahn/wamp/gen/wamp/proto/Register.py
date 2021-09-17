# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class Register(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRegister(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Register()
        x.Init(buf, n + offset)
        return x

    # Register
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Register
    def Request(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Register
    def Procedure(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Register
    def Match(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Register
    def Invoke(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Register
    def Concurrency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Register
    def ForceReregister(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def RegisterStart(builder): builder.StartObject(6)
def RegisterAddRequest(builder, request): builder.PrependUint64Slot(0, request, 0)
def RegisterAddProcedure(builder, procedure): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(procedure), 0)
def RegisterAddMatch(builder, match): builder.PrependUint8Slot(2, match, 0)
def RegisterAddInvoke(builder, invoke): builder.PrependUint8Slot(3, invoke, 0)
def RegisterAddConcurrency(builder, concurrency): builder.PrependUint16Slot(4, concurrency, 0)
def RegisterAddForceReregister(builder, forceReregister): builder.PrependBoolSlot(5, forceReregister, 0)
def RegisterEnd(builder): return builder.EndObject()
