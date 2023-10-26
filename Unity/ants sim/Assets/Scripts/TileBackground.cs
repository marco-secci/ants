using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TileBackground : MonoBehaviour
{

    // Defining variables:
    public GameObject tilePrefab;
    public int rows = 10;
    public int cols = 10;
    public float tileSize = 1.0f;

    // Start is called before the first frame update
    void Start()
    {
        GenerateGrid();
    }

    // Creating the grid with tiles:
    void GenerateGrid()
    {

        if (tilePrefab == null)
        {
        Debug.LogError("Tile prefab is not assigned!");
        return;
        }

        // Creating the grid: 
        for (int x = 0; x < cols; x++)
        {
            for (int y = 0; y < rows; y++)
            {
                GameObject tile = Instantiate(tilePrefab, transform);
                float posX = x * tileSize;
                float posY = y * tileSize;
                tile.transform.position = new Vector2(posX, posY);
            }
        }
    }
}