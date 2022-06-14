// Auto-generated. Do not edit!

// (in-package darknet_ros_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class classes {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.glass_num = null;
      this.long_hair_num = null;
      this.glass_cut_num = null;
      this.long_hair_cut_num = null;
      this.short_hair_num = null;
      this.short_hair_cut_num = null;
    }
    else {
      if (initObj.hasOwnProperty('glass_num')) {
        this.glass_num = initObj.glass_num
      }
      else {
        this.glass_num = 0;
      }
      if (initObj.hasOwnProperty('long_hair_num')) {
        this.long_hair_num = initObj.long_hair_num
      }
      else {
        this.long_hair_num = 0;
      }
      if (initObj.hasOwnProperty('glass_cut_num')) {
        this.glass_cut_num = initObj.glass_cut_num
      }
      else {
        this.glass_cut_num = 0;
      }
      if (initObj.hasOwnProperty('long_hair_cut_num')) {
        this.long_hair_cut_num = initObj.long_hair_cut_num
      }
      else {
        this.long_hair_cut_num = 0;
      }
      if (initObj.hasOwnProperty('short_hair_num')) {
        this.short_hair_num = initObj.short_hair_num
      }
      else {
        this.short_hair_num = 0;
      }
      if (initObj.hasOwnProperty('short_hair_cut_num')) {
        this.short_hair_cut_num = initObj.short_hair_cut_num
      }
      else {
        this.short_hair_cut_num = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type classes
    // Serialize message field [glass_num]
    bufferOffset = _serializer.int16(obj.glass_num, buffer, bufferOffset);
    // Serialize message field [long_hair_num]
    bufferOffset = _serializer.int16(obj.long_hair_num, buffer, bufferOffset);
    // Serialize message field [glass_cut_num]
    bufferOffset = _serializer.int16(obj.glass_cut_num, buffer, bufferOffset);
    // Serialize message field [long_hair_cut_num]
    bufferOffset = _serializer.int16(obj.long_hair_cut_num, buffer, bufferOffset);
    // Serialize message field [short_hair_num]
    bufferOffset = _serializer.int16(obj.short_hair_num, buffer, bufferOffset);
    // Serialize message field [short_hair_cut_num]
    bufferOffset = _serializer.int16(obj.short_hair_cut_num, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type classes
    let len;
    let data = new classes(null);
    // Deserialize message field [glass_num]
    data.glass_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [long_hair_num]
    data.long_hair_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [glass_cut_num]
    data.glass_cut_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [long_hair_cut_num]
    data.long_hair_cut_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [short_hair_num]
    data.short_hair_num = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [short_hair_cut_num]
    data.short_hair_cut_num = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'darknet_ros_msgs/classes';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '807f252bc3466dd12378a82941c798f7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 glass_num  
    int16 long_hair_num
    int16 glass_cut_num
    int16 long_hair_cut_num
    int16 short_hair_num
    int16 short_hair_cut_num
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new classes(null);
    if (msg.glass_num !== undefined) {
      resolved.glass_num = msg.glass_num;
    }
    else {
      resolved.glass_num = 0
    }

    if (msg.long_hair_num !== undefined) {
      resolved.long_hair_num = msg.long_hair_num;
    }
    else {
      resolved.long_hair_num = 0
    }

    if (msg.glass_cut_num !== undefined) {
      resolved.glass_cut_num = msg.glass_cut_num;
    }
    else {
      resolved.glass_cut_num = 0
    }

    if (msg.long_hair_cut_num !== undefined) {
      resolved.long_hair_cut_num = msg.long_hair_cut_num;
    }
    else {
      resolved.long_hair_cut_num = 0
    }

    if (msg.short_hair_num !== undefined) {
      resolved.short_hair_num = msg.short_hair_num;
    }
    else {
      resolved.short_hair_num = 0
    }

    if (msg.short_hair_cut_num !== undefined) {
      resolved.short_hair_cut_num = msg.short_hair_cut_num;
    }
    else {
      resolved.short_hair_cut_num = 0
    }

    return resolved;
    }
};

module.exports = classes;
