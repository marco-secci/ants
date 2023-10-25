using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AntAnimation : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Script 'AntAnimation' started");
    }

    public float rotationSpeed = 50f;
    // Update is called once per frame
    void Update()
    {
        transform.Rotate(Vector3.forward, rotationSpeed * Time.deltaTime);
        Debug.Log("Ant Rotation Update");
    }
}
