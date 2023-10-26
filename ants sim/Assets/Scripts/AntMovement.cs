using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AntMovement : MonoBehaviour
{

    public float speed = 5.0f;
    public float rotationSpeed = 2.0f;
    // public float rotationThreshold = 0.1f;

    private Vector3 target;
    // private bool isRotating = false; 

    // Start is called before the first frame update:
    void Start()
    {
        // Current Ant position:
        target = transform.position;
        Debug.Log("Script 'AntMovement' started. ");
    }

    // Update is called once per frame
    void Update()
    {
        // If left click:
        if (Input.GetMouseButton(0))
        {
            // Converting click into coordinates:
            target = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            target.z = transform.position.z;
            // isRotating = true;
        }

        // Calculating angle to rotate:
        Vector3 direction = target - transform.position;
        float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;

        // Rotating towards the mouse click:
        Quaternion targetRotation = Quaternion.AngleAxis(angle - 90, Vector3.forward);
        transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, rotationSpeed * Time.deltaTime);

        // Rotation is complete! Yay!
        // if (Quaternion.Angle(transform.rotation, targetRotation) < rotationThreshold)
            
        // isRotating = false;
        // Move ant towards target:
        transform.position = Vector3.MoveTowards(transform.position, target, speed * Time.deltaTime);
        //public float newSpeed = speed;
        
    }
}
