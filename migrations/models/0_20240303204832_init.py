from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `b_hospital` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT 'UUID',
    `hospital_name` VARCHAR(256) NOT NULL  COMMENT '医院名称',
    `address` VARCHAR(512) NOT NULL  COMMENT '医院地址',
    `herd_towards_enthusiasm` DECIMAL(8,2)   COMMENT '大众对医院的热度'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_hospital_doctor_tags` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT 'UUID',
    `tag_name` VARCHAR(64) NOT NULL  COMMENT '医生专长标签' DEFAULT '请填入'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_hospital_doctors` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT 'UUID',
    `doctor_name` VARCHAR(24) NOT NULL  COMMENT '医师姓名',
    `contact` VARCHAR(16) NOT NULL  COMMENT '联系方式(手机)',
    `hospital_belong_id` VARCHAR(36) NOT NULL,
    CONSTRAINT `fk_b_hospit_b_hospit_deb1e305` FOREIGN KEY (`hospital_belong_id`) REFERENCES `b_hospital` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_hospital_tags` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT 'UUID',
    `tag_name` VARCHAR(64) NOT NULL  COMMENT '医院标签' DEFAULT '请填入'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_kv` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `label` VARCHAR(64) NOT NULL  COMMENT '标签',
    `key` VARCHAR(2) NOT NULL  COMMENT '键，数字',
    `value` VARCHAR(64) NOT NULL  COMMENT '值，数字代表的含义'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_recommended_nutrition_in_take` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT 'UUID',
    `in_take_case_name` VARCHAR(32) NOT NULL  COMMENT '摄入项目',
    `recommended_lower_limit` DECIMAL(8,2) NOT NULL  COMMENT '建议摄入最小值',
    `recommended_upper_limit` DECIMAL(8,2) NOT NULL  COMMENT '建议摄入最大值',
    `metric` VARCHAR(10) NOT NULL  COMMENT '计量单位'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user_tags` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `tag_name` VARCHAR(64) NOT NULL  COMMENT '用户标签' DEFAULT '请填入'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `username` VARCHAR(64) NOT NULL  COMMENT '用户名' DEFAULT '用户d5G9',
    `user_type` VARCHAR(1) NOT NULL  COMMENT '0表示普通用户, 1表示管理员' DEFAULT '0',
    `phone` VARCHAR(14) NOT NULL  COMMENT '注册手机号' DEFAULT '',
    `password` VARCHAR(200) NOT NULL  COMMENT '密码，经过Base64加密',
    `avatar` VARCHAR(1024) NOT NULL  COMMENT '用户头像地址' DEFAULT '',
    `grade` INT NOT NULL  COMMENT '用户等级' DEFAULT 1,
    `grade_accumulate` INT NOT NULL  COMMENT '用户积分/经验' DEFAULT 0,
    `status` VARCHAR(1) NOT NULL  COMMENT '停用状态0正常1停用' DEFAULT '0',
    `self_description` VARCHAR(300) NOT NULL  COMMENT '个人简介' DEFAULT '这个人很懒，还没有介绍...',
    `ip_region` VARCHAR(256) NOT NULL  COMMENT 'ip归属地' DEFAULT '未知',
    `urgent_contract` VARCHAR(14) NOT NULL  COMMENT '紧急联系人手机号' DEFAULT ''
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user_medicine_history` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `illness_name` VARCHAR(256) NOT NULL  COMMENT '病名',
    `begin_time` DATE NOT NULL  COMMENT '生病开始时间',
    `duration` VARCHAR(1)   COMMENT '持续时间0一个月内1一到三个月2三至半年4半年至一年5一年至三年6三年以上',
    `medicine` VARCHAR(256)   COMMENT '用药情况',
    `user_id_id` BIGINT UNSIGNED NOT NULL,
    CONSTRAINT `fk_b_user_m_b_user_cd155df6` FOREIGN KEY (`user_id_id`) REFERENCES `b_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user_physical` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `rel_name` VARCHAR(256) NOT NULL  COMMENT '真实姓名',
    `gender` VARCHAR(1) NOT NULL  COMMENT '用户性别0男1女2未知' DEFAULT '0',
    `birthday` DATE NOT NULL  COMMENT '出生年月日',
    `identity_card` VARCHAR(20) NOT NULL  COMMENT '身份证号',
    `address` VARCHAR(256) NOT NULL  COMMENT '居住地',
    `weight` DECIMAL(6,2) NOT NULL  COMMENT '体重/kg',
    `height` DECIMAL(6,2) NOT NULL  COMMENT '身高/cm',
    `blood_type` VARCHAR(1) NOT NULL  COMMENT '血型0A1B2AB3O',
    `user_id_id` BIGINT UNSIGNED NOT NULL,
    CONSTRAINT `fk_b_user_p_b_user_3da5f31e` FOREIGN KEY (`user_id_id`) REFERENCES `b_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user_in_take` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64) NOT NULL  COMMENT '创建人',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT '2024-03-03T20:48:31.648140',
    `modify_by` VARCHAR(64) NOT NULL  COMMENT '修改人',
    `modify_time` DATETIME(6) NOT NULL  COMMENT '修改时间',
    `remark` VARCHAR(500) NOT NULL  COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `calorie` DECIMAL(10,2) NOT NULL  COMMENT '摄入热量，单位cal',
    `uploaded_image` VARCHAR(1024) NOT NULL  COMMENT '用户上传的食物图片',
    `recognized_object` VARCHAR(512) NOT NULL  COMMENT '识别到的照片的内容' DEFAULT '',
    `upload_time` DATETIME(6) NOT NULL  COMMENT '上传时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id_id` BIGINT UNSIGNED NOT NULL,
    CONSTRAINT `fk_b_user_i_b_user_db87985f` FOREIGN KEY (`user_id_id`) REFERENCES `b_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_hospital_b_hospital_tags` (
    `b_hospital_id` VARCHAR(36) NOT NULL,
    `hospitaltags_id` VARCHAR(36) NOT NULL,
    FOREIGN KEY (`b_hospital_id`) REFERENCES `b_hospital` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`hospitaltags_id`) REFERENCES `b_hospital_tags` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_hospital_doctors_b_hospital_doctor_tags` (
    `b_hospital_doctors_id` VARCHAR(36) NOT NULL,
    `hospitaldoctorproficiencytags_id` VARCHAR(36) NOT NULL,
    FOREIGN KEY (`b_hospital_doctors_id`) REFERENCES `b_hospital_doctors` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`hospitaldoctorproficiencytags_id`) REFERENCES `b_hospital_doctor_tags` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `b_user_b_user_tags` (
    `b_user_id` BIGINT UNSIGNED NOT NULL,
    `usertags_id` BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`b_user_id`) REFERENCES `b_user` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`usertags_id`) REFERENCES `b_user_tags` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
