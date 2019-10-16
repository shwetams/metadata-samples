package com.ms.cse.api.service;

import java.io.IOException;

public interface ApiService {

	
	String callApi(String method, String inputJSON, String aPIUrl) throws IOException, Exception;

	String callApi(String method, String aPIUrl) throws IOException;

}

