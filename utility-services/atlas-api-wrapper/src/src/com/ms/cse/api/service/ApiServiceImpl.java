package com.ms.cse.api.service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import com.ms.cse.api.apiApp;
import com.ms.cse.api.conf.Constants;

import sun.misc.BASE64Encoder;

@Service
public class ApiServiceImpl implements ApiService {
	private static final Logger LOG = LoggerFactory.getLogger(ApiServiceImpl.class);

	@Override
	public String callApi(String method, String inputJSON, String aPIUrl) throws IOException  {

		String atlasServerIP = Constants.ATLASSERVERIP;
		String atlasServerPort = Constants.ATLASSERVERPORT;
		String userName = Constants.USERNAME;
		String password = Constants.PASSWORD;

		URL url = null;
		
			url = new URL("http://" + atlasServerIP + ":" + atlasServerPort + "/api/atlas/" + aPIUrl);
		
		HttpURLConnection conn = null;

			conn = (HttpURLConnection) url.openConnection( );
		
		conn.setDoOutput(true);

			conn.setRequestMethod(method);
		
		conn.setRequestProperty("Content-Type", "application/json");

		BASE64Encoder enc = new sun.misc.BASE64Encoder();
		String userpassword = userName + ":" + password;
		String encodedAuthorization = enc.encode(userpassword.getBytes()).replaceAll("(\\r|\\n)", "");;
		conn.setRequestProperty("Authorization", "Basic " + encodedAuthorization);

		String input = inputJSON;

		OutputStream os;
		BufferedReader br = null ;
		
			os = conn.getOutputStream();
			os.write(input.getBytes());
			os.flush();
			System.out.println(conn.getResponseCode());
			if (200 <= conn.getResponseCode() && conn.getResponseCode() <= 299) {
			    br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			} else {
			    br = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
			}
			
		String output = null;
		String result="";
		System.out.println("Output from Server .... \n");
		
			while ((output = br.readLine()) != null) {
				LOG.info("output String : " +output);
				result+=output;
			}
		
		conn.disconnect();
		return result;

	}

	
	@Override
	public String callApi(String method, String aPIUrl) throws IOException {

		String atlasServerIP = Constants.ATLASSERVERIP;
		String atlasServerPort = Constants.ATLASSERVERPORT;
		String userName = Constants.USERNAME;
		String password = Constants.PASSWORD;

		// apiurl=v2/types/typedefs

		URL url = new URL("http://" + atlasServerIP + ":" + atlasServerPort + "/api/atlas/" + aPIUrl);
		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		conn.setDoOutput(true);
		conn.setRequestMethod(method);
		conn.setRequestProperty("Content-Type", "application/json");

		BASE64Encoder enc = new sun.misc.BASE64Encoder();
		String userpassword = userName + ":" + password;
		String encodedAuthorization = enc.encode(userpassword.getBytes()).replaceAll("(\\r|\\n)", "");;
		conn.setRequestProperty("Authorization", "Basic " + encodedAuthorization);
		
		BufferedReader br = null ;
		
		if (200 <= conn.getResponseCode() && conn.getResponseCode() <= 299) {
		    br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
		} else {
		    br = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
		}


		//LOG.info(conn.getResponseCode() + ":" + conn.getResponseMessage());

		//BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));

		String output;
		String result="";
		System.out.println("Output from Server .... \n");
		while ((output = br.readLine()) != null) {
			LOG.info(output);
			result+=output;
		}

		conn.disconnect();
		return result;

	}

}
