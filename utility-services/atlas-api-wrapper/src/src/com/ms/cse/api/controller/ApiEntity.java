package com.ms.cse.api.controller;


import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.Logger;

import org.slf4j.LoggerFactory;

import com.ms.cse.api.service.ApiService;

@RestController
public class ApiEntity {

	private static final Logger LOG = LoggerFactory.getLogger(ApiEntity.class);
	@Autowired
	ApiService apiService;
	
	

	
	@PostMapping("/api/entity")
	public String entityPost(@RequestBody String ipJSON) {
		try {
			return apiService.callApi("POST", ipJSON, "v2/entity");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
		}
		
	}
	
	
	@GetMapping("/api/entity/bulk")
	public String entityBulkGet(@RequestBody String ipJSON) {
		try {
			return apiService.callApi("GET", ipJSON, "v2/entity/bulk");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
		}
		
	}
	
	@DeleteMapping("/api/entity/bulk")
	public String entityBulkDelete(@RequestBody String ipJSON) {
		try {
			return apiService.callApi("DELETE", ipJSON, "v2/entity/bulk");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
		}
		
	}
	
	@PostMapping("/api/entity/bulk")
	public String entityBulkPost(@RequestBody String ipJSON) {
		try {
			return apiService.callApi("POST", ipJSON, "v2/entity/bulk");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
		}
		
	}
	
	
	
}