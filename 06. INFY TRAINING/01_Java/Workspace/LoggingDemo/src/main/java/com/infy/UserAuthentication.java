package com.infy;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class UserAuthentication {

	Log logger1 = LogFactory.getLog(UserAuthentication.class);

	public void loginUser(String username, String password) throws Exception {
		try {
			if (username.isBlank() || password.isBlank()) {
				throw new Exception("Service.INVALID_CREDENTIALS");
			}
			logger1.info(username + " logged in successfully");
		} catch (Exception exception) {
			logger1.error(exception.getMessage(), exception);
			throw exception;
		}
	}
}
