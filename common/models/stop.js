module.exports = function(Stop) {
	Stop.disableRemoteMethod("create", true);
	Stop.disableRemoteMethod("upsert", true);
	Stop.disableRemoteMethod("updateAll", true);
	Stop.disableRemoteMethod("updateAttributes", false);
	Stop.disableRemoteMethod("find", true);
	Stop.disableRemoteMethod("findById", true);
	Stop.disableRemoteMethod("findOne", true);
	Stop.disableRemoteMethod("deleteById", true);
	Stop.disableRemoteMethod("confirm", true);
	Stop.disableRemoteMethod("count", true);
	Stop.disableRemoteMethod("exists", true);
	Stop.disableRemoteMethod("resetPassword", true);
	Stop.disableRemoteMethod('createChangeStream', true);
	Stop.disableRemoteMethod('__delete__logs', false);
	Stop.disableRemoteMethod('__updateById__logs', false);
	Stop.disableRemoteMethod('__destroyById__logs', false);
};
