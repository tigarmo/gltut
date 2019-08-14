#version 330 core

in vec2 pos;
out vec3 color;

uniform float light_x;

vec3 compute_lighting(in vec3 normal)
{
    vec3 lightDir = normalize(vec3(0.0, 1.0, 1.0));
    float lightIntensity = 1.0;

    vec3 surfaceNormal = normalize(normal);
    float cosAngIncidence = dot(surfaceNormal, lightDir);
    cosAngIncidence = cosAngIncidence < 0.0001 ? 0.0 : cosAngIncidence;

    vec3 diffuse = vec3(1.0, 1.0, 1.0);
    vec3 ambient = vec3(1.0) * 0.05;

    vec3 lighting = diffuse * lightIntensity * cosAngIncidence;
    lighting += ambient;

    return lighting;
}

void main(){
    float dist = dot(pos, pos);
    if (dist > 1.0)
        discard;

    color = vec3(1,0,0);

    float z = sqrt(1.0f - dist);
    vec3 normal = vec3(pos, z);

    color *= compute_lighting(normal);
}