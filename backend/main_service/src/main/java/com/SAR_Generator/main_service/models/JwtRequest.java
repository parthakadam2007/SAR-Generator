package com.SAR_Generator.main_service.models;


import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
public class JwtRequest {
    private String email;
    private String password;
    private String role;
}
