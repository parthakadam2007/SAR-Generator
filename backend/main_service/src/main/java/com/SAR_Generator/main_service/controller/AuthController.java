package com.SAR_Generator.main_service.controller;

import java.util.UUID;
import java.util.logging.Logger;

import com.SAR_Generator.main_service.services.user.UserSerivceImple;
import org.apache.kafka.common.security.oauthbearer.internals.secured.JwtResponseParser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.SAR_Generator.main_service.dto.UserDTO;
import com.SAR_Generator.main_service.models.JwtRequest;
import com.SAR_Generator.main_service.models.JwtResponse;
import com.SAR_Generator.main_service.security.JWTHelper;
import com.SAR_Generator.main_service.services.user.UserSerivce;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @Autowired
    private UserDetailsService userDetailsService;

    @Autowired
    private AuthenticationManager manager;

    @Autowired
    private JWTHelper helper;

    @Autowired
    private UserSerivceImple userSerivceImple;

    @Autowired
    private   PasswordEncoder passwordEncoder;


    // private Logger logger = Logger.getLogger(AuthController.class);

    @PostMapping("/login/analyst")
    public ResponseEntity<JwtResponse> userLogin(@RequestBody JwtRequest request) {
        this.doAuthenticate(request.getEmail(), request.getPassword());
        UserDTO userInfo = userSerivceImple.getUserByEmail(request.getEmail());
        UserDetails userDetails = userDetailsService.loadUserByUsername(request.getEmail());
        String token = this.helper.generateToken(userDetails, userInfo.id());

        JwtResponse response = JwtResponse.builder()
                        .jwtToken(token)
                        .username(userDetails.getUsername())
                        .userId(userInfo.id()).build();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

    @PostMapping("/signup/analyst")
    public  ResponseEntity<JwtResponse> userSignup(@RequestBody JwtRequest request) {
        if(request.getEmail() == null || request.getEmail().isEmpty() || request.getPassword() == null || request.getPassword().isEmpty()){
            throw new RuntimeException("Email cannot be null or empty");
        }
        String hashed = passwordEncoder.encode(request.getPassword());
        UserDTO userInfo = UserDTO.builder()
                .email(request.getEmail())
                .password(request.getPassword())
                .username("Partha")
                .build();

        UserDTO userDTO = userSerivceImple.
                saveUser(userInfo);


        this.doAuthenticate(request.getEmail(), request.getPassword());
        UserDetails userDetails = userDetailsService.loadUserByUsername(request.getEmail());
        String token  = this.helper.generateToken(userDetails, userDTO.id());
        JwtResponse response = JwtResponse.builder()
            .jwtToken(token)
            .username(userDetails.getUsername())
            .userId(userDTO.id())
            .build();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

    private void doAuthenticate(String email, String password) {
    UsernamePasswordAuthenticationToken authentication =
            new UsernamePasswordAuthenticationToken(email, password);
    try {
        manager.authenticate(authentication);
    } catch (BadCredentialsException e) {
        throw new BadCredentialsException(" Invalid email or Password  !!");
    }
    }
    

    
    
    
}
