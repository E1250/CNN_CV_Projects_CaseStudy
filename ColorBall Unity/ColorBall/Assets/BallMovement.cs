using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallMovement : MonoBehaviour
{

    public UDPReceive udbReceive;



    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = udbReceive.data;
        // ex..(x, y, area) -- (255, 361, 50012) 

        // Removing Bracets `()`
        data = data.Remove(0, 1); // Deleting range
        data = data.Remove(data.Length - 1, 1); // Deleting range

        // Splitting numbers
        string[] info = data.Split(',');

        // String to Float with normalization
        float x = 5 - float.Parse(info[0]) / 100;
        float y = float.Parse(info[1]) / 100;
        float z = -10 +float.Parse(info[2]) / 1000; // area

        // set data to object
        gameObject.transform.localPosition = new Vector3(x, y, z);

    }
}
