from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `b_recommended_perform` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64)   COMMENT '创建人',
    `create_time` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `modify_by` VARCHAR(64)   COMMENT '修改人',
    `modify_time` DATETIME(6)   COMMENT '修改时间',
    `remark` VARCHAR(500)   COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `exam_item` VARCHAR(255) NOT NULL  COMMENT '体检项目名称',
    `exam_recommended_perform` DECIMAL(10,2) NOT NULL  COMMENT '数据表现',
    `exam_metric` VARCHAR(32) NOT NULL  COMMENT '数据单位'
) CHARACTER SET utf8mb4;
        ALTER TABLE `b_user_physical` MODIFY COLUMN `height` DECIMAL(6,2)   COMMENT '身高/cm';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `address` VARCHAR(256)   COMMENT '居住地';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `weight` DECIMAL(6,2)   COMMENT '体重/kg';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `blood_type` VARCHAR(1)   COMMENT '血型0A1B2AB3O';
        CREATE TABLE IF NOT EXISTS `b_user_physical_examination` (
    `del_flag` VARCHAR(1) NOT NULL  COMMENT '删除标记0存在1删除' DEFAULT '0',
    `create_by` VARCHAR(64)   COMMENT '创建人',
    `create_time` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `modify_by` VARCHAR(64)   COMMENT '修改人',
    `modify_time` DATETIME(6)   COMMENT '修改时间',
    `remark` VARCHAR(500)   COMMENT '备注',
    `id` BIGINT UNSIGNED NOT NULL  PRIMARY KEY COMMENT 'snowflake-id',
    `exam_item` VARCHAR(255) NOT NULL  COMMENT '体检项目名称',
    `exam_perform` DECIMAL(10,2) NOT NULL  COMMENT '数据表现',
    `exam_metric` VARCHAR(32) NOT NULL  COMMENT '数据单位',
    `exam_recommended_perform` DECIMAL(10,2) NOT NULL  COMMENT '正常数据表现',
    `exam_standard_id` BIGINT UNSIGNED NOT NULL,
    `user_id_id` BIGINT UNSIGNED NOT NULL,
    CONSTRAINT `fk_b_user_p_b_recomm_dd066b71` FOREIGN KEY (`exam_standard_id`) REFERENCES `b_recommended_perform` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_b_user_p_b_user_4f9981e4` FOREIGN KEY (`user_id_id`) REFERENCES `b_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
        ALTER TABLE `b_user` ALTER COLUMN `username` SET DEFAULT '用户pgZg';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `b_user` ALTER COLUMN `username` SET DEFAULT '用户Naom';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `height` DECIMAL(6,2) NOT NULL  COMMENT '身高/cm';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `address` VARCHAR(256) NOT NULL  COMMENT '居住地';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `weight` DECIMAL(6,2) NOT NULL  COMMENT '体重/kg';
        ALTER TABLE `b_user_physical` MODIFY COLUMN `blood_type` VARCHAR(1) NOT NULL  COMMENT '血型0A1B2AB3O';
        DROP TABLE IF EXISTS `b_recommended_perform`;
        DROP TABLE IF EXISTS `b_user_physical_examination`;"""
