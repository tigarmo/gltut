#version 330 core

in vec2 pos;
out vec3 color;

void main(){
    float dist = dot(pos, pos);
    //if (dist > 1.0)
        //discard;

    if (pos.x < 0.0)
        color = vec3(0,1,0);
    else
        color = vec3(1,0,0);

}